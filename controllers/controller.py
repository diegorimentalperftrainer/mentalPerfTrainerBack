from flask import Blueprint, jsonify, request
from database.repositories.questionRepository import QuestionRepository

questionRepository = QuestionRepository()

globalBp = Blueprint('questionBp', __name__)

@globalBp.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questionRepository.get_questions_for_front())

@globalBp.route('/answers', methods=['POST'])
def submit_answers():
    data = request.get_json()
    user = data['user']
    answers = data['answers']
    print(user)
    print(answers)

    return jsonify({"status": "ok"}), 200