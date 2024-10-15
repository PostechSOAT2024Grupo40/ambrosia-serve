from typing import List

from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway
from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class PostgreSqlProductGateway(IProductGateway):

    def __init__(self, uow: IProductUnitOfWork):
        super().__init__()
        self.uow = uow

    def get_products(self) -> List[Product]:
        with self.uow as uow:
            products = uow.repository.get_all()
            return [Product(**p) for p in products]

    def get_product_by_sku(self, sku: str) -> Product:
        with self.uow as uow:
            product = uow.repository.filter_by_sku(sku)
            return Product(**product)

    def create_update_product(self, product: Product) -> Product:
        with self.uow as uow:
            uow.repository.insert_update({'id': product.id,
                                          'sku': product.sku,
                                          'category': product.category,
                                          'description': product.description,
                                          'stock': product.stock,
                                          'price': product.price})
            uow.commit()
            return product

    def delete_product(self, sku: str) -> None:
        with self.uow as uow:
            uow.repository.delete(sku)
            uow.commit()
