from abc import ABC
from typing import Any, List

from src.domain.entities.user import User


class IUserPresenter(ABC):

    def user_present(self, output: User | List[User]) -> Any:
        ...
