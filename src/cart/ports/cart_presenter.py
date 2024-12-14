from abc import ABC, abstractmethod
from typing import Any

from src.cart.domain.entities.order import Order


class ICartPresenter(ABC):

    @abstractmethod
    def present(self, output: Order | list[Order]) -> Any:
        ...
