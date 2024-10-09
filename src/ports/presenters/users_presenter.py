from abc import ABC
from typing import Any

from src.domain.entities.user import User


class ICreateNewUserPresenter(ABC):

    def present(self, output: User) -> Any:
        ...
