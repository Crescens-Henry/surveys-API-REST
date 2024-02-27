from flask import Blueprint, jsonify
from User.Application.DeleteUserUseCase import DeleteUserUseCase

delete_user_blueprint = Blueprint('delete_user', __name__)

def initialize_endpoints(repositorio):
    deleteUserUseCase = DeleteUserUseCase(repositorio)

    @delete_user_blueprint.route('/<int:id>', methods=['DELETE'])
    def delete_user(id):
        deleteUserUseCase.execute(id)
        return jsonify({'message': 'User deleted'}), 200