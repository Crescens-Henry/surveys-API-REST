from flask import Blueprint, request, jsonify
from User.Application.listUsersUseCase import ListUsersUseCase

get_list_users_blueprint = Blueprint('get_list_users', __name__)

def initialize_endpoints(repositorio):
    listUsersUseCase = ListUsersUseCase(repositorio)

    @get_list_users_blueprint.route('/', methods=['GET'])
    def get_list_users():
        users = listUsersUseCase.execute()
        users = [user.to_dict() for user in users]
        return jsonify(users), 200