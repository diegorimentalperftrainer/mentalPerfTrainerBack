from infrastructure.database.repositories.question_repository import QuestionRepository

question_repository = QuestionRepository()

def get_questions_for_front():
    return question_repository.get_questions_for_front()