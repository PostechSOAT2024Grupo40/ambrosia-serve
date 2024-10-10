from typing import Any, Dict

from src.client.domain.entities.user import User
from src.client.domain.validators.user_validator import UserValidator
from src.client.exceptions import UserExistsError, UserNotFoundError
from src.client.ports.user_gateway import IUserGateway


class UsersUseCase:
    @staticmethod
    def create_new_user(request_data: Dict, gateway: IUserGateway) -> Any:
        if UsersUseCase.get_user_by_cpf(cpf=request_data["cpf"], gateway=gateway):
            raise UserExistsError(user=request_data["cpf"])

        user = User(first_name=request_data["first_name"],
                    last_name=request_data["last_name"],
                    cpf=request_data["cpf"],
                    email=request_data["email"],
                    password=request_data["password"])

        return gateway.create_user(user)

    @staticmethod
    def update_user(request_data: Dict, gateway: IUserGateway) -> Any:
        user_ = UsersUseCase.get_user_by_cpf(cpf=request_data["cpf"], gateway=gateway)
        if not user_:
            raise UserNotFoundError(user=request_data["cpf"])

        user_.first_name = request_data["first_name"]
        user_.last_name = request_data["last_name"]
        user_.cpf = request_data["cpf"]
        user_.email = request_data["email"]
        user_.password = request_data["password"]

        UserValidator.validate_user(user_)

        return gateway.update_user(user_)

    @staticmethod
    def delete_user(user_id: int, gateway: IUserGateway):
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
