from abc import ABC, abstractmethod
from typing import List

from src.client.domain.entities.user import User
from src.client.ports.unit_of_work_interface import IClientUnitOfWork


class IUserGateway(ABC):
    uow: IClientUnitOfWork

    @abstractmethod
    def get_users(self) -> List[User]:
        ...

    @abstractmethod
    def get_user_by_cpf(self, cpf: str) -> User:
        ...

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        ...

    @abstractmethod
    def create_user(self, user: User) -> User:
        ...

    @abstractmethod
    def update_user(self, user: User) -> User:
        ...

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        ...

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        ...
