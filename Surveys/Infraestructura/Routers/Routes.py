from Surveys.Infraestructura.Controllers.CreateSurveyController import create_survey_blueprint, initialize_endpoints as initialize_endpoints_create_survey
from Surveys.Infraestructura.Controllers.DeleteSurveyController import delete_survey_blueprint, initialize_endpoints as initialize_endpoints_delete_survey
from Surveys.Infraestructura.Controllers.GetSurveyByIdController import get_survey_blueprint, initialize_endpoints as initialize_endpoints_getId_survey
from Surveys.Infraestructura.Controllers.ListSurveyController import get_list_survey_blueprint, initialize_endpoints as initialize_endpoints_get_list_survey
from Surveys.Infraestructura.Controllers.UpdateSurveyController import update_survey_blueprint, initialize_endpoints as initialize_endpoints_update_survey

def initialize_app(app,repository):
    initialize_endpoints_create_survey(repository)
    initialize_endpoints_delete_survey(repository)
    initialize_endpoints_getId_survey(repository)
    initialize_endpoints_get_list_survey(repository)
    initialize_endpoints_update_survey(repository)

    app.register_blueprint(create_survey_blueprint, url_prefix="/create-survey")
    app.register_blueprint(delete_survey_blueprint,url_prefix="/delete-survey")
    app.register_blueprint(get_survey_blueprint,url_prefix="/get-survey")
    app.register_blueprint(get_list_survey_blueprint,url_prefix="/get-list-survey")
    app.register_blueprint(update_survey_blueprint,url_prefix="/update-survey")


