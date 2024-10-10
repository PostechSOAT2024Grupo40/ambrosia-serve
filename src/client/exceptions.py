class UserExistsError(Exception):
    def __init__(self, user):
        super().__init__(f"O usuário {user} ja existe")


class UserNotFoundError(Exception):
    def __init__(self, user):
        super().__init__(f"O usuário {user} não existe")


class AddressExistsError(Exception):
    def __init__(self, address):
        super().__init__(f"O endereço {address} ja existe")


class AddressNotFoundError(Exception):
    def __init__(self, address):
        super().__init__(f"O endereço {address} não existe")
