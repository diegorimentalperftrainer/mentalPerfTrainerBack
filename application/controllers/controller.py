from flask import Blueprint, jsonify, request
from application.services import answer_service, question_service

globalBp = Blueprint('questionBp', __name__)

@globalBp.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(question_service.get_questions_for_front())

@globalBp.route('/answers', methods=['POST'])
def submit_answers():
    data = request.get_json()
    answer_service.handle_answers(data)
    return jsonify({"status": "ok"}), 200