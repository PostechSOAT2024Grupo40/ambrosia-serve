from typing import Any, Dict

from src.domain.entities.user import User
from src.ports.gateways.user_gateway import IUserGateway
from src.shared.exceptions import UserExistsError, UserNotFoundError


class UsersUseCase:

    @staticmethod
    def create_new_user(request_data: Dict, gateway: IUserGateway) -> Any:
        if UsersUseCase.get_user_by_cpf(cpf=request_data["cpf"], gateway=gateway):
            raise UserExistsError(user=request_data["cpf"])

        user = User(first_name=request_data["first_name"],
                    last_name=request_data["last_name"],
                    cpf=request_data["cpf"],
                    email=request_data["email"],
                    password=request_data["password"],
                    address=request_data["address"])

        return gateway.create_user(user)

    @staticmethod
    def update_user(request_data: Dict, gateway: IUserGateway) -> Any:
        if not UsersUseCase.get_user_by_cpf(cpf=request_data["cpf"], gateway=gateway):
            raise UserNotFoundError(user=request_data["cpf"])

        user = User(first_name=request_data["first_name"],
                    last_name=request_data["last_name"],
                    cpf=request_data["cpf"],
                    email=request_data["email"],
                    password=request_data["password"],
                    address=request_data["address"])

        return gateway.update_user(user)

    @staticmethod
    def delete_user(user_id: int, gateway: IUserGateway) -> Any:
        user = gateway.get_user_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundError(user=user_id)

        gateway.delete_user(user.id)

    @staticmethod
    def get_user_by_cpf(cpf: str, gateway: IUserGateway) -> Any:
        return gateway.get_user_by_cpf(cpf)

    @staticmethod
    def get_users(gateway: IUserGateway) -> Any:
        return gateway.get_users()
