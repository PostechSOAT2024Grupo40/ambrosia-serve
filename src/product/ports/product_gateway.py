from abc import ABC, abstractmethod
from typing import List

from src.product.domain.entities.product import Product


class IProductGateway(ABC):

    @abstractmethod
    def get_products(self) -> List[Product]:
        ...

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        ...

    @abstractmethod
    def create_update_product(self, product: Product) -> Product:
        ...

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        ...
