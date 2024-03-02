from flask import Blueprint, request, jsonify
from Surveys.Application.CreateSurveyUseCase import CreateSurveyUseCase
from Surveys.Domain.Entities.ASurvey import ASurvey

import requests

create_survey_blueprint = Blueprint('create_survey', __name__)

def initialize_endpoints(repository):
    create_survey_use_case = CreateSurveyUseCase(repository)

    @create_survey_blueprint.route('/', methods=['POST'])
    def create_survey():
        survey_data = request.get_json()
        
        # Extraer las preguntas del JSON
        asks_data = survey_data.pop('asks', [])

        # Crear la encuesta con la lista de preguntas vacía
        survey = ASurvey(**survey_data)

        # Ejecutar el caso de uso para crear la encuesta
        success, result = create_survey_use_case.execute(survey)
        
        if success:
            # Obtener el ID de la encuesta
            survey_uuid = result.survey_uuid # Suponiendo que result contiene la encuesta creada
            
            # Llamar al controlador de pregunta para crear las preguntas asociadas
            for ask_data in asks_data:
                # Agregar el ID de la encuesta a los datos de la pregunta
                ask_data['survey_uuid'] = survey_uuid
                
                # Llamar al controlador de pregunta y pasarle los datos
                requests.post('http://localhost:5000/create-ask/', json=ask_data)
            
            return jsonify({"message": "Survey created", "survey": result.to_dict()}), 200
        else:
            return jsonify({"message": "Error creating survey", "error": result}), 400