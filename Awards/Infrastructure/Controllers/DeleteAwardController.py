from flask import Blueprint, jsonify
from Awards.Application.DeleteAwardUseCase import DeleteAwardUseCase

delete_award_blueprint = Blueprint('delete_award', __name__)

def initialize_endpoints(repository):
    deleteAwardUseCase = DeleteAwardUseCase(repository)

    @delete_award_blueprint.route('/<int:id>', methods=['DELETE'])
    def delete_award(id):
        deleteAwardUseCase.execute(id)
        return jsonify({'message': 'Award deleted'}), 200