from src.client.exceptions import UserNotFoundError
from src.client.ports.user_gateway import IUserGateway


class DeleteUserUseCase:
    def __init__(self, gateway: IUserGateway):
        self.gateway = gateway

    def execute(self, user_id: str) -> None:
        user = self.gateway.get_user_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundError(user=user_id)

        self.gateway.delete_user(user_id)
