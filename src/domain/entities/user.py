import uuid
from typing import List

from src.domain.validators.user_validator import UserValidator


class User:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 cpf: str,
                 email: str,
                 password: str,
                 address: List[str]):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.email = email
        self.password = password
        self.address = address

        UserValidator.validate_user(user=self)
