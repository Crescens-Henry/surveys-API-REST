from User.Domain.Entities.User import User as UserDomain

class SignInUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user: UserDomain):
        user_exist = self.repository.getByEmail(user.credentials.email)
        if user_exist is not None:
            return False, {"error": "El correo electrónico ya está en uso."}
        try:
            self.repository.save(user)
            return True, user
        except Exception as e:
            return False, {"error": str(e)}