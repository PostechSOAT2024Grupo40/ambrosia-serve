from abc import ABC, abstractmethod
from typing import Any, List

from src.client.domain.entities.user import User


class IUserPresenter(ABC):

    @abstractmethod
    def present(self, output: User | List[User]) -> Any:
        ...
