from src.client.domain.entities.user import User
from src.client.domain.validators.user_validator import UserValidator
from src.client.exceptions import UserNotFoundError
from src.client.ports.user_gateway import IUserGateway


class UpdateUserUseCase:
    def __init__(self, gateway: IUserGateway):
        self.gateway = gateway

    def execute(self, request_data: dict[str, str]) -> User:
        user_ = self.gateway.get_user_by_cpf(cpf=request_data["cpf"])
        if not user_:
            raise UserNotFoundError(user=request_data["cpf"])

        user_.first_name = request_data["first_name"]
        user_.last_name = request_data["last_name"]
        user_.cpf = request_data["cpf"]
        user_.email = request_data["email"]
        user_.password = request_data["password"]

        UserValidator.validate_user(user_)

        return self.gateway.update_user(user_)
