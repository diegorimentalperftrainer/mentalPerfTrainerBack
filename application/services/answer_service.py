from application.constants import email
from application.helpers import create_graph
from infrastructure.database.repositories.category_repository import CategoryRepository
from infrastructure.database.repositories.question_repository import QuestionRepository
from infrastructure.externals.mail_sender import MailContext, mail_sender
from datetime import datetime
from config import Config

category_repository = CategoryRepository()
question_repository = QuestionRepository()

def handle_answers(data):
    user = User(data['user'])
    answers = extract_all_answers(data['answers'])
    categories = category_repository.get_categories()
    questions = question_repository.get_questions()
    scores_by_categories = []
    question_map = {q.id: q for q in questions}
    for category in categories:
        category_result = handle_category(category, questions, answers, question_map)
        scores_by_categories.append(category_result)
    filename = "{}_{}.png".format(user.get_full_name().replace(' ', "_"), datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    chart_path = create_graph.generate_chart(scores_by_categories, filename)
    send_mail_to_user(user, chart_path)
    send_mail_to_admin(user, chart_path)

def handle_category(category, questions, answers, question_map):
    filtered_questions = [question for question in questions if question.category_id == category.id]
    filtered_questions_ids = [question.id for question in filtered_questions]
    filtered_answers = [answer for answer in answers if answer.question_id in filtered_questions_ids]
    if len(filtered_answers) > 0:
        total = 0
        for answer in filtered_answers:
            if question_map[answer.question_id].revers:
                total += (6 - answer.value)
            else:
                total += answer.value
        average = total / len(filtered_answers)
    else:
        average = 0
    return CategoryResult(category.french_label, category.competition, average)

def send_mail_to_user(user, chart_path):
    mail_context = MailContext(email.USER_SUBJECT, user.email, email.USER_BODY, email.USER_FROM_NAME, chart_path)
    mail_sender.send_mail(mail_context)

def send_mail_to_admin(user, chart_path):
    subject = email.ADMIN_SUBJECT.replace("FULLNAME", user.get_full_name())
    body = email.ADMIN_BODY.replace("FULLNAME", user.get_full_name())
    mail_context = MailContext(subject, Config.ADMIN_MAIL, body, email.ADMIN_FROM_NAME, chart_path)
    mail_sender.send_mail(mail_context)

def extract_all_answers(front_answers):
    answers = []
    for answer in front_answers:
        answers.append(Answer(answer))
    return answers


class Answer:
    def __init__(self, answer):
        self.question_id = answer['questionId']
        self.value = answer['value']

class User:
    def __init__(self, user):
        self.last_name = user['lastName']
        self.first_name = user['firstName']
        self.email = user['email']

    def get_full_name(self):
        return self.last_name.upper() + ' ' + self.first_name.title()

class CategoryResult:
    def __init__(self, name, competition, score):
        self.name = name
        self.competition = competition
        self.score = score
