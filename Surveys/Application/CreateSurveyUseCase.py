from Surveys.Domain.Entity.Asurvey import Asurvey

class CreateSurveyUseCase:
    def __init__(self, repository):
        self.repository = repository

    def create_survey(self, survey: Asurvey):
       self.repositorio.save(survey)
       return survey