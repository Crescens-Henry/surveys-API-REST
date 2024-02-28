from User.Domain.Entities.AUser import User as UserDomain
from User.Infrastructure.security.utils import get_hashed_password

class SignUpUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user: UserDomain):
        user_exist = self.repository.getByEmail(user.credentials.email)
        if user_exist is not None:
            return False, {"error": "El correo electrónico ya está en uso."}
        try:
            user.credentials.password = get_hashed_password(user.credentials.password)
            self.repository.save(user)
            return True, user
        except Exception as e:
            return False, {"error": str(e)}