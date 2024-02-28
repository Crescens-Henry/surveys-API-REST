from flask import Blueprint, request, jsonify
from User.Application.SignInUseCase import SignInUseCase

signin_blueprint = Blueprint('user_signIn', __name__)

def initialize_endpoints(repositorio):
    signInUsercase = SignInUseCase(repositorio)

    @signin_blueprint.route('/', methods=['POST'])
    def user_signIn():
        user_data = request.get_json()
        email = user_data['email']
        password = user_data['password']
        token = signInUsercase.execute(email, password)
        if token:
            return jsonify({"mensaje": "Sistema dice", "token": token}), 200
        else:
            return jsonify({"mensaje": "Credenciales incorrectas"}), 400