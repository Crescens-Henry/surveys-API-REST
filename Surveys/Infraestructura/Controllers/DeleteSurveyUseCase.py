from flask import Blueprint, jsonify
from Surveys.Application.DeleteSurveyUseCase import DeleteSurveyUseCase

delete_survey_blueprint = Blueprint('delete_survey', __name__)


def initialize_endpoints(repositorio):
    deleteSurveyUseCase = DeleteSurveyUseCase(repositorio)

    @delete_survey_blueprint.route('/<int:id>', methods=['DELETE'])
    def delete_survey(id):
        deleteSurveyUseCase.execute(id)
        return jsonify({'message': 'survey deleted'}), 200