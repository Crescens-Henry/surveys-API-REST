from Surveys.Application.GetSurveyUseCase import GetSurveyUseCase
from flask import Blueprint, request, jsonify, abort

get_survey_blueprint = Blueprint('get_survey', __name__)

def initialize_endpoints(repository):
    getSurveyUseCase = GetSurveyUseCase(repository)

    @get_survey_blueprint.route('/<int:id>', methods=['GET'])
    def get_survey(id):
        survey = getSurveyUseCase.execute(id)
        if survey is None:
             return jsonify({"message": "Error "}), 400
        return jsonify(survey.to_dict()), 200