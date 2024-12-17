from abc import ABC, abstractmethod
from typing import Any

from src.client.domain.entities.user import User


class IUserPresenter(ABC):

    @abstractmethod
    def present(self, output: User | list[User]) -> Any:
        ...
