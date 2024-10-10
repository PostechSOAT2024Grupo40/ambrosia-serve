import uuid

from src.client.domain.validators.user_validator import UserValidator


class User:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 cpf: str,
                 email: str,
                 password: str):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.email = email
        self.password = password

        UserValidator.validate_user(user=self)

    def __hash__(self):
        return hash(self.cpf)

    def __eq__(self, other):
        return self.cpf == other.cpf
