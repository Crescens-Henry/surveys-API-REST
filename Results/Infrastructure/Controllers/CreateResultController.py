from flask import Blueprint, request, jsonify
from Results.Domain.Entities.AResult import AResult
from Results.Application.CreateResultUseCase import CreateResultUseCase

create_result_blueprint = Blueprint('create_result', __name__)

def initialize_endpoints(repository):
    create_result_use_case = CreateResultUseCase(repository)

    @create_result_blueprint.route('/', methods=['POST'])
    def create_result():
        try:
            result_data = request.get_json()
            success, result = create_result_use_case.execute(AResult(**result_data))
            
            if success:
                return jsonify({"message": "Result created", "result": result}), 200
            else:
                return jsonify({"message": "Error creating result", "error": result}), 400
        except Exception as e:
            return jsonify({"message": "Error creating result", "error": str(e)}), 400