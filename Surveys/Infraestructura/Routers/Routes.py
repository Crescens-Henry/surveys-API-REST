from Surveys.Infraestructura.Controllers.CreateSurveyController import create_survey_blueprint, initialize_endpoints as initialize_endpoints_create_survey
from Surveys.Infraestructura.Controllers.DeleteSurveyController import delete_survey_blueprint, initialize_endpoints as initialize_endpoints_delete_survey
from Surveys.Infraestructura.Controllers.GetSurveyByIdController import get_survey_blueprint,initialize_endpoints as initialize_endpoints_getId_survey

def initialize_app(app,repository):
    initialize_endpoints_create_survey(repository)
    initialize_endpoints_delete_survey(repository)
    initialize_endpoints_getId_survey(repository)

    app.register_blueprint(create_survey_blueprint, url_prefix="/create-survey")
    app.register_blueprint(delete_survey_blueprint,url_prefix="/delete-survey")
    app.register_blueprint(get_survey_blueprint,url_prefix="/get-survey/")

