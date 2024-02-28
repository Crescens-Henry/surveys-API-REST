from User.Infrastructure.Repositories.MysqlRepository import Repository as UserRepository
from Awards.Infrastructure.Repositories.MysqlRepository import Repository as AwardRepository

from Surveys.Infraestructura.Repositories.MysqlRepository import Repository as SurveyRepository
from Surveys.Infraestructura.Routers.Routes import initialize_app as initialize_app_survey

from User.Infrastructure.Routes.Routes import initialize_app as initialize_app_user
from Awards.Infrastructure.Routes.Routes import initialize_app as initialize_app_award
from flask import Flask

app = Flask(__name__)

repository_user = UserRepository()
repository_award = AwardRepository()
repository_survey = SurveyRepository()

initialize_app_user(app, repository_user)
initialize_app_award(app, repository_award)
initialize_app_survey(app, repository_survey)

if __name__ == "__main__":
    app.run(debug=True)