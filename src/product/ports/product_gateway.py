from abc import ABC, abstractmethod
from typing import List

from src.product.domain.entities.product import Product
from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class IProductGateway(ABC):
    uow: IProductUnitOfWork

    @abstractmethod
    def get_products(self) -> List[Product]:
        ...

    @abstractmethod
    def get_product_by_sku(self, sku: str) -> Product:
        ...
        

    @abstractmethod
    def create_update_product(self, product: Product) -> Product:
        ...

    @abstractmethod
    def delete_product(self, sku: str) -> None:
        ...
