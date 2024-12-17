from src.client.domain.entities.user import User
from src.client.ports.user_gateway import IUserGateway


class GetAllUsersUseCase:
    def __init__(self, gateway: IUserGateway):
        self.gateway = gateway

    def execute(self) -> list[User]:
        return self.gateway.get_users()
