from flask import Blueprint, jsonify
from Awards.Application.DeleteAwardUseCase import DeleteAwardUseCase

delete_award_blueprint = Blueprint('delete_award', __name__)

def initialize_endpoints(repository):
    deleteAwardUseCase = DeleteAwardUseCase(repository)

    @delete_award_blueprint.route('/<int:id>', methods=['DELETE'])
    def delete_award(id):
        try:
            deleteAwardUseCase.execute(id)
            return jsonify({'message': 'Award deleted'}), 200
        except Exception as e:
            return jsonify({"message": "Error deleting award", "error": str(e)}), 400