class ListSurveyUseCase:
    def __init__(self, surveyRepository):
        self.surveyRepository = surveyRepository

    def execute(self):
        return self.surveyRepository.getAll()