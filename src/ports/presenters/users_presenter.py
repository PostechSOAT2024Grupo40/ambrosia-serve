from abc import ABC, abstractmethod
from typing import Any, List

from src.domain.entities.user import User


class IUserPresenter(ABC):

    @abstractmethod
    def user_present(self, output: User | List[User]) -> Any:
        ...
