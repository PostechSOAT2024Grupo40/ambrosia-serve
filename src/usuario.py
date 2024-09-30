import re
import uuid
from typing import List

from src.domain_exception import DomainException


class Usuario:
    def __init__(self,
                 nome: str,
                 sobrenome: str,
                 cpf: str,
                 email: str,
                 senha: str,
                 enderecos: List[str]):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.enderecos = enderecos

        self.__validador()

    def __validador(self):
        self.__email_validator()

        self.__senha_validator()

        self.__cpf_validator()

        self.__nome_sobrenome_validator()

    def __nome_sobrenome_validator(self):
        if not self.nome or not self.nome.strip():
            raise DomainException("Nome não pode ser vazio")
        if not self.sobrenome or not self.sobrenome.strip():
            raise DomainException("Sobrenome não pode ser vazio")

    def __cpf_validator(self):
        if not self.cpf or not self.cpf.strip():
            raise DomainException("CPF não pode ser vazio")
        if re.match(r"[0-9]{11}", self.cpf) is None:
            raise DomainException("CPF inválido")

    def __senha_validator(self):
        if not self.senha or not self.senha.strip():
            raise DomainException("Senha não pode ser vazia")
        if len(self.senha) < 8:
            raise DomainException("Senha deve ter pelo menos 8 caracteres")

    def __email_validator(self):
        if not self.email or not self.email.strip():
            raise DomainException("Email não pode ser vazio")
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email) is None:
            raise DomainException("Email inválido")
