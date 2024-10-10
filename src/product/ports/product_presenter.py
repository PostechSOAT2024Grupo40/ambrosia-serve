from abc import ABC, abstractmethod
from typing import Any, List

from src.product.domain.entities.product import Product


class IProductPresenter(ABC):

    @abstractmethod
    def present(self, output: Product | List[Product]) -> Any:
        ...
