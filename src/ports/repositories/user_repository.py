from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_cpf(self, cpf: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: str) -> User:
        raise NotImplementedError
