from typing import Dict

from src.client.domain.entities.user import User
from src.client.exceptions import UserExistsError
from src.client.ports.user_gateway import IUserGateway


class CreateUserUseCase:
    def __init__(self, gateway: IUserGateway):
        self.gateway = gateway

    def execute(self, request_data: Dict) -> User:
        if self.gateway.get_user_by_cpf(cpf=request_data["cpf"]):
            raise UserExistsError(user=request_data["cpf"])

        user = User(first_name=request_data["first_name"],
                    last_name=request_data["last_name"],
                    cpf=request_data["cpf"],
                    email=request_data["email"],
                    password=request_data["password"])

        return self.gateway.create_user(user)
