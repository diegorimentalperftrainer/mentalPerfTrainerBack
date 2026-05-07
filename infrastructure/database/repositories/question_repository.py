from infrastructure.database.models.question import Question

class QuestionRepository:

    @staticmethod
    def get_questions_for_front():
        questions = Question.query.order_by(Question.id).all()
        return [q.to_dict_for_front() for q in questions]

    @staticmethod
    def get_questions():
        return Question.query.all()