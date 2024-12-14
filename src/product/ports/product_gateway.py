from abc import ABC, abstractmethod

from src.product.domain.entities.product import Product
from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class IProductGateway(ABC):
    uow: IProductUnitOfWork

    @abstractmethod
    def get_products(self) -> list[Product]:
        ...

    @abstractmethod
    def get_product_by_id(self, product_id: str) -> Product:
        ...

    @abstractmethod
    def create_update_product(self, product: Product) -> Product:
        ...

    @abstractmethod
    def delete_product(self, product_id: str) -> None:
        ...
    @abstractmethod
    def get_product_by_name(self, product_name:str):
        ...
