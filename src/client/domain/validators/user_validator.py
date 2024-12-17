import re

from src.client.domain.domain_exception import ClientDomainException


class UserValidator:

    @staticmethod
    def validate_user(user):
        UserValidator._email_validator(user)

        UserValidator._password_validator(user)

        UserValidator._cpf_validator(user)

        UserValidator._first_and_last_name_validator(user)

    @staticmethod
    def _first_and_last_name_validator(user):
        if not user.first_name or not user.first_name.strip():
            raise ClientDomainException("Nome não pode ser vazio")
        if not user.last_name or not user.last_name.strip():
            raise ClientDomainException("Sobrenome não pode ser vazio")

    @staticmethod
    def _cpf_validator(user):
        if not user.cpf or not user.cpf.strip():
            raise ClientDomainException("CPF não pode ser vazio")
        if re.match(r"\d{11}", user.cpf) is None:
            raise ClientDomainException("CPF inválido")

    @staticmethod
    def _password_validator(user):
        if not user.password or not user.password.strip():
            raise ClientDomainException("Senha não pode ser vazia")
        if len(user.password) < 8:
            raise ClientDomainException("Senha deve ter pelo menos 8 caracteres")

    @staticmethod
    def _email_validator(user):
        if not user.email or not user.email.strip():
            raise ClientDomainException("Email não pode ser vazio")
        if re.match(r"[^@]+@[^@]+\.[^@]+", user.email) is None:
            raise ClientDomainException("Email inválido")
