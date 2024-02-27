from flask import Blueprint, request, jsonify
from User.Application.SignInUseCase import SignInUseCase
from User.Domain.Entities.User import User
from User.Domain.Entities.Contact import Contact
from User.Domain.Entities.Credentials import Credentials

signin_blueprint = Blueprint('user_signIn', __name__)

def initialize_endpoints(repositorio):
    createUserUsercase = SignInUseCase(repositorio)

    @signin_blueprint.route('/', methods=['POST'])
    def user_signIn():
        user_data = request.get_json()
        contact = Contact(name=user_data['name'], last_name=user_data['last_name'], phone=user_data['phone'])
        credentials = Credentials(email=user_data['email'], password=user_data['password'])
        user = User(contact=contact, credentials=credentials)
        usuario_creado, mensaje = createUserUsercase.execute(user)
        if usuario_creado:
            return jsonify({"mensaje": "Sistema dice", "usuario": usuario_creado}), 200
        else:
            return jsonify({"mensaje": mensaje["error"]}), 400