from flask import Blueprint, request, jsonify
from Awards.Application.UpdateAwardUseCase import UpdateAwardUseCase

update_award_blueprint = Blueprint('update_award', __name__)

def initialize_endpoints(repository):
    updateAwardUseCase = UpdateAwardUseCase(repository)

    @update_award_blueprint.route('/<int:id>', methods=['PUT'])
    def update_award(id):
        try:
            award_data = request.get_json()
            award = updateAwardUseCase.execute(id, award_data)
            return jsonify(award.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error updating award", "error": str(e)}), 400