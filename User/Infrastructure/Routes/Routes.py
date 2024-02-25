from flask import Flask
from User.Infrastructure.Controllers.SignInController import crear_usuario_blueprint, initialize_endpoints

app = Flask(__name__)

def initialize_app(repositorio):
    initialize_endpoints(repositorio)
    app.register_blueprint(crear_usuario_blueprint, url_prefix="/signin")