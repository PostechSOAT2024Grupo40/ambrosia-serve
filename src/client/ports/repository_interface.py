from abc import ABC, abstractmethod
from typing import Any


class IClientRepository(ABC):

    @abstractmethod
    def get_users(self) -> list[Any]:
        ...

    @abstractmethod
    def get_user_by_cpf(self, cpf: str) -> Any:
        ...

    @abstractmethod
    def get_user_by_email(self, email: str) -> Any:
        ...

    @abstractmethod
    def create_user(self, user: Any):
        ...

    @abstractmethod
    def update_user(self, user: Any):
        ...

    @abstractmethod
    def delete_user(self, user_id: str):
        ...

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Any:
        ...
