from flask import Blueprint, request, jsonify
from Surveys.Application.GetSurveyUseCase import GetSurveyUseCase

get_survey_status_blueprint = Blueprint('get_survey_status', __name__)

def initialize_endpoints(repository):
    getSurveyUseCase = GetSurveyUseCase(repository)

    @get_survey_status_blueprint.route('/<int:id>', methods=['GET'])
    def get_pot_survey_status(id):
        try:
            # Usar el caso de uso para obtener la encuesta con todo su contenido
            survey = getSurveyUseCase.execute(id)

            # Lista para almacenar los resultados de la comparación
            comparison_results = []

            # Iterar sobre cada pregunta en la encuesta
            for ask in survey.asks:
                # Obtener los datos de CorrectResult
                correct_result_data = {
                    'valueUno': ask.correct_result.valueUno,
                    'valueDos': ask.correct_result.valueDos
                }
                
                # Obtener los datos de Result
                result_data = {
                    'valorUno': ask.result.valorUno,
                    'valorDos': ask.result.valorDos
                }
                
                # Comparar los datos de CorrectResult y Result
                comparison_result = correct_result_data == result_data
                
                # Agregar el resultado de la comparación a la lista
                comparison_results.append(comparison_result)

            # Retorna los resultados de comparación en formato JSON
            return jsonify({"comparison_results": comparison_results}), 200
        
        except Exception as e:
            # En caso de error, retorna un mensaje de error
            return jsonify({"message": "Error processing request", "error": str(e)}), 400
