from Surveys.Infraestructura.Controllers.CreateSurveyController import create_survey_blueprint, initialize_endpoints as initialize_endpoints_create_survey
from Surveys.Infraestructura.Controllers.DeleteSurveyController import delete_survey_blueprint, initialize_endpoints as initialize_endpoints_delete_survey
from Surveys.Infraestructura.Controllers.GetSurveyByIdController import get_survey_blueprint, initialize_endpoints as initialize_endpoints_getId_survey
from Surveys.Infraestructura.Controllers.ListSurveyController import get_list_survey_blueprint, initialize_endpoints as initialize_endpoints_get_list_survey
from Surveys.Infraestructura.Controllers.UpdateSurveyController import update_survey_blueprint, initialize_endpoints as initialize_endpoints_update_survey
#-----ASK
from Surveys.Infraestructura.Controllers.CreateAskController import create_ask_blueprint, initialize_endpoints as initialize_endpoints_create_ask
from Surveys.Infraestructura.Controllers.DeleteAskController import delete_ask_blueprint,initialize_endpoints as initialize_endpoints_delete_ask
from Surveys.Infraestructura.Controllers.GetAskByIdController import get_ask_blueprint, initialize_endpoints as initialize_endpoints_getId_ask
from Surveys.Infraestructura.Controllers.ListAskController import get_list_ask_blueprint, initialize_endpoints as initialize_endpoints_get_list_ask
from Surveys.Infraestructura.Controllers.UpdateAskController import update_ask_blueprint, initialize_endpoints as initialize_endpoints_update_ask


def initialize_app(app,repository):
    initialize_endpoints_create_survey(repository)
    initialize_endpoints_delete_survey(repository)
    initialize_endpoints_getId_survey(repository)
    initialize_endpoints_get_list_survey(repository)
    initialize_endpoints_update_survey(repository)

    initialize_endpoints_create_ask(repository)
    initialize_endpoints_delete_ask(repository)
    initialize_endpoints_getId_ask(repository)
    initialize_endpoints_get_list_ask(repository)
    initialize_endpoints_update_ask(repository)

    app.register_blueprint(create_ask_blueprint,url_prefix="/create-ask")
    app.register_blueprint(delete_ask_blueprint,url_prefix="/delete-ask")
    app.register_blueprint(get_ask_blueprint,url_prefix="/get-ask")
    app.register_blueprint(get_list_ask_blueprint,url_prefix="/get-list-ask")
    app.register_blueprint(update_ask_blueprint,url_prefix="/update-ask")

    app.register_blueprint(create_survey_blueprint, url_prefix="/create-survey")
    app.register_blueprint(delete_survey_blueprint,url_prefix="/delete-survey")
    app.register_blueprint(get_survey_blueprint,url_prefix="/get-survey")
    app.register_blueprint(get_list_survey_blueprint,url_prefix="/get-list-survey")
    app.register_blueprint(update_survey_blueprint,url_prefix="/update-survey")


    

