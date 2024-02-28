from flask import Blueprint, request, jsonify
from User.Application.SignUpUseCase import SignUpUseCase
from User.Domain.Entities.AUser import User
from User.Domain.Entities.Contact import Contact
from User.Domain.Entities.Credentials import Credentials
from User.Domain.Entities.UserType import UserType

signup_blueprint = Blueprint('user_signUp', __name__)

def initialize_endpoints(repositorio):
    createUserUsercase = SignUpUseCase(repositorio)

    @signup_blueprint.route('/', methods=['POST'])
    def user_signUp():
        user_data = request.get_json()
        contact = Contact(name=user_data['name'], last_name=user_data['last_name'], phone=user_data['phone'])
        credentials = Credentials(email=user_data['email'], password=user_data['password'])
        user_type= UserType(user_data['type'].upper())
        user = User(contact=contact, credentials=credentials, type=user_type)
        usuario_creado, mensaje = createUserUsercase.execute(user)
        if usuario_creado:
            return jsonify({"mensaje": "Sistema dice", "usuario": usuario_creado}), 200
        else:
            return jsonify({"mensaje": mensaje["error"]}), 400