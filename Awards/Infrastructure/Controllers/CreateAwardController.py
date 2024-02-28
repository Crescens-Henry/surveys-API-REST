from flask import Blueprint, request, jsonify
from Awards.Application.CreateAwardUseCase import CreateAwardUseCase
from Awards.Domain.Entities.AAward import AAward

create_award_blueprint = Blueprint('create_award', __name__)

def initialize_endpoints(repository):
    create_award_use_case = CreateAwardUseCase(repository)

    @create_award_blueprint.route('/', methods=['POST'])
    def create_award():
        try:
            award_data = request.get_json()
            success, result = create_award_use_case.execute(AAward(**award_data))
            
            if success:
                return jsonify({"message": "Award created", "award": result}), 200
            else:
                return jsonify({"message": "Error creating award", "error": result}), 400
        except Exception as e:
            return jsonify({"message": "Error creating award", "error": str(e)}), 400