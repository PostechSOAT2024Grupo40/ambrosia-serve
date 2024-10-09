from typing import List, Dict, Optional
from src.client.domain.entities.user import User
from src.client.ports.gateways.user_gateway import IUserGateway
from src.client.exceptions import UserExistsError, UserNotFoundError

class MockUserGateway(IUserGateway):
    def __init__(self):
        self.users_by_cpf: Dict[str, User] = {}
        self.users_by_id: Dict[str, User] = {}

    def get_users(self) -> List[User]:
        return list(self.users_by_id.values())

    def get_user_by_cpf(self, cpf: str) -> Optional[User]:
        return self.users_by_cpf.get(cpf)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users_by_id.values() if user.email == email), None)

    def create_user(self, user: User) -> User:
        if user.cpf in self.users_by_cpf:
            raise UserExistsError(user=user.cpf)
        self.users_by_cpf[user.cpf] = user
        self.users_by_id[user.id] = user
        return user

    def update_user(self, user: User) -> User:
        if user.cpf not in self.users_by_cpf:
            raise UserNotFoundError(user=user.cpf)
        self.users_by_cpf[user.cpf] = user
        self.users_by_id[user.id] = user
        return user

    def delete_user(self, user_id: int) -> None:
        user = self.users_by_id.pop(user_id, None)
        if user:
            self.users_by_cpf.pop(user.cpf, None)

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        return self.users_by_id.get(user_id)
