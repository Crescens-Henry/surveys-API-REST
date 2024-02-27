class ListUsersUseCase:
    def __init__(self, userRepository):
        self.userRepository = userRepository

    def execute(self):
        return self.userRepository.getAll()