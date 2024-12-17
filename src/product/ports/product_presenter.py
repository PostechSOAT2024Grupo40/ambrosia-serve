from abc import ABC, abstractmethod
from typing import Any

from src.product.domain.entities.product import Product


class IProductPresenter(ABC):

    @abstractmethod
    def present(self, output: Product | list[Product]) -> Any:
        ...
