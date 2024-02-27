from flask import Flask
from User.Infrastructure.Controllers.SignUpController import signup_blueprint, initialize_endpoints as initialize_endpoints_signup
from User.Infrastructure.Controllers.ListUserController import get_list_users_blueprint, initialize_endpoints as initialize_endpoints_list_users
from User.Infrastructure.Controllers.GetUserByIdController import get_user_blueprint, initialize_endpoints as initialize_endpoints_get_user
from User.Infrastructure.Controllers.UpdateUserController import update_user_blueprint, initialize_endpoints as initialize_endpoints_update_user
from User.Infrastructure.Controllers.DeleteUserController import delete_user_blueprint, initialize_endpoints as initialize_endpoints_delete_user

app = Flask(__name__)

def initialize_app(repositorio):
    initialize_endpoints_signup(repositorio)
    initialize_endpoints_list_users(repositorio)
    initialize_endpoints_get_user(repositorio)
    initialize_endpoints_update_user(repositorio)
    initialize_endpoints_delete_user(repositorio)
    
    app.register_blueprint(signup_blueprint, url_prefix="/signup")
    app.register_blueprint(get_list_users_blueprint, url_prefix="/list-users")
    app.register_blueprint(get_user_blueprint, url_prefix="/get-user")
    app.register_blueprint(update_user_blueprint, url_prefix="/update-user")
    app.register_blueprint(delete_user_blueprint, url_prefix="/delete-user")