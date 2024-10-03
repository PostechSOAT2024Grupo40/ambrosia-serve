import re
import uuid
from typing import List

from src.domain.domain_exception import DomainException


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

        self.__validador()

    def __validador(self):
        self.__email_validator()

        self.__password_validator()

        self.__cpf_validator()

        self.__first_and_last_name_validator()

    def __first_and_last_name_validator(self):
        if not self.first_name or not self.first_name.strip():
            raise DomainException("Nome não pode ser vazio")
        if not self.last_name or not self.last_name.strip():
            raise DomainException("Sobrenome não pode ser vazio")

    def __cpf_validator(self):
        if not self.cpf or not self.cpf.strip():
            raise DomainException("CPF não pode ser vazio")
        if re.match(r"[0-9]{11}", self.cpf) is None:
            raise DomainException("CPF inválido")

    def __password_validator(self):
        if not self.password or not self.password.strip():
            raise DomainException("Senha não pode ser vazia")
        if len(self.password) < 8:
            raise DomainException("Senha deve ter pelo menos 8 caracteres")

    def __email_validator(self):
        if not self.email or not self.email.strip():
            raise DomainException("Email não pode ser vazio")
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email) is None:
            raise DomainException("Email inválido")
