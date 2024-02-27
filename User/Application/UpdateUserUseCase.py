class UpdateUserUseCase:
    def __init__(self, repository):
        self.repositorio = repository

    def execute(self, id, user_data):
        user = self.repositorio.get_by_id(id)
        if user is None:
            raise Exception('User not found')
        else:
            updated_user = self.repositorio.update(id, user_data)
            return updated_user