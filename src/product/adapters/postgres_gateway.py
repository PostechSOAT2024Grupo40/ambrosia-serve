from typing import List, Optional

from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway
from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class PostgreSqlProductGateway(IProductGateway):

    def __init__(self, uow: IProductUnitOfWork):
        super().__init__()
        self.uow = uow

    def get_products(self) -> List[Product]:
        with self.uow:
            products = self.uow.repository.get_all()
            return [self.build_product_entity(p) for p in products]

    def get_product_by_sku(self, sku: str) -> Optional[Product]:
        with self.uow:
            product = self.uow.repository.filter_by_sku(sku)
            if not product:
                return
            return self.build_product_entity(product)

    @staticmethod
    def build_product_entity(product):
        return Product(_id=product['id'],
                       sku=product['sku'],
                       description=product['description'],
                       category=product['category'],
                       price=product['price'],
                       stock=product['stock'])

    def create_update_product(self, product: Product) -> Product:
        with self.uow:
            self.uow.repository.insert_update({'id': product.id,
                                               'sku': product.sku,
                                               'category': product.category,
                                               'description': product.description,
                                               'stock': product.stock,
                                               'price': product.price})
            self.uow.commit()
            return product

    def delete_product(self, sku: str) -> None:
        with self.uow:
            self.uow.repository.delete(sku)
            self.uow.commit()
