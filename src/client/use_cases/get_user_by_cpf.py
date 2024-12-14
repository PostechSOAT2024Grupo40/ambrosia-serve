from typing import Optional

from src.client.domain.entities.user import User
from src.client.ports.user_gateway import IUserGateway


class GetUserByCpfUseCase:
    def __init__(self, gateway: IUserGateway):
        self.gateway = gateway

    def execute(self, cpf: str) -> Optional[User]:
        return self.gateway.get_user_by_cpf(cpf=cpf)
