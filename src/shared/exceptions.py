class UserExistsError(Exception):
    def __init__(self, user):
        super().__init__(f"O usuário {user} ja existe")


class UserNotFoundError(Exception):
    def __init__(self, user):
        super().__init__(f"O usuário {user} não existe")
