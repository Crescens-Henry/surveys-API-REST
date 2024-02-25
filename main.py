from User.Infrastructure.Repositories.MysqlRepository import Repositorio as UserRepository
from User.Infrastructure.Routes.Routes import app, initialize_app

repositorio = UserRepository()

initialize_app(repositorio)

if __name__ == "__main__":
    app.run(debug=True)