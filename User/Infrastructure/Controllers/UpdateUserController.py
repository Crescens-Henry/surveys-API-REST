from flask import Blueprint, request, jsonify
from User.Application.UpdateUserUseCase import UpdateUserUseCase

update_user_blueprint = Blueprint('update_user', __name__)

def initialize_endpoints(repository):
    updateUserUseCase = UpdateUserUseCase(repository)

    @update_user_blueprint.route('/<int:id>', methods=['PUT'])
    def update_user(id):
        user_data = request.get_json()
        user = updateUserUseCase.execute(id, user_data)
        return jsonify(user.to_dict()), 200