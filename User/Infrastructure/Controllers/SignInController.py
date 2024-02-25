from flask import Blueprint, request
from User.Application.SignInUseCase import SignInUseCase
from User.Domain.Entities.User import User
from User.Domain.Entities.Contact import Contact
from User.Domain.Entities.Credentials import Credentials

crear_usuario_blueprint = Blueprint('crear_usuario', __name__)

def initialize_endpoints(repositorio):
    createUserUsercase = SignInUseCase(repositorio)

    @crear_usuario_blueprint.route('/', methods=['POST'])
    def crear_usuario():
        user_data = request.get_json()
        contact = Contact(name=user_data['name'], last_name=user_data['last_name'], phone=user_data['phone'])
        credentials = Credentials(email=user_data['email'], password=user_data['password'])
        user = User(contact=contact, credentials=credentials)
        usuario_creado = createUserUsercase.execute(user)
        return {"mensaje": "Sistema dice", "\nusuario": usuario_creado}