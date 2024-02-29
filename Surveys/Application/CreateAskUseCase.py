from Surveys.Domain.Entities.ask import Ask as AskDomain 

class CreateAskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, ask: AskDomain):
       ask_exist = self.repository.get_by_ask(ask.ask)
       if ask_exist is not None:
        return False, {"error": "it already exists."}
       
       try:
        self.repository.save_ask(ask)
        return True, ask
       
       except Exception as e:
        return False, {"error": str(e)}