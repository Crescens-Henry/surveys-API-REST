from flask import Blueprint, request, jsonify
from Surveys.Application.CreateSurveyUseCase import CreateSurveyUseCase
from Surveys.Domain.Entities.ASurvey import ASurvey


create_survey_blueprint = Blueprint('create_survey', __name__)


def initialize_endpoints(repository):
    create_survey_use_case = CreateSurveyUseCase(repository)

    @create_survey_blueprint.route('/', methods=['POST'])
    def create_survey():
        survey_data = request.get_json()
        
        success, result = create_survey_use_case.execute(ASurvey(**survey_data))
        
        if success:
            return jsonify({"message": "Survey created", "survey": result}), 200
        else:
            return jsonify({"message": "Error creating survey", "error": result}), 400