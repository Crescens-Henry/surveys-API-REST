from flask import Blueprint, request, jsonify
from Awards.Application.GetAwardUseCase import GetAwardUseCase

get_Award_blueprint = Blueprint('get_award', __name__)

def initialize_endpoints(repository):
    getAwardUseCase = GetAwardUseCase(repository)

    @get_Award_blueprint.route('/<int:id>', methods=['GET'])
    def get_award(id):
        try:
            award = getAwardUseCase.execute(id)
            return jsonify(award.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error getting award", "error": str(e)}), 400