from typing import Optional

from sqlalchemy import Row

from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway
from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class PostgreSqlProductGateway(IProductGateway):

    def __init__(self, uow: IProductUnitOfWork):
        super().__init__()
        self.uow = uow

    def get_products(self) -> list[Product]:
        with self.uow:
            products = self.uow.repository.get_all()
            return [self.build_product_entity(p[0]) for p in products]

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        with self.uow:
            product = self.uow.repository.filter_by_id(product_id)
            if not product:
                return
            return self.build_product_entity(product)

    def get_product_by_name(self, name: str) -> Optional[Product]:
        with self.uow:
            product = self.uow.repository.find_by_name(name)
            if not product:
                return
            return self.build_product_entity(product)

    @staticmethod
    def build_product_entity(product: Row):
        return Product(_id=product.id,
                       name=product.name,
                       description=product.description,
                       category=product.category,
                       price=product.price,
                       image=product.image,
                       stock=product.stock)

    def create_update_product(self, product: Product) -> Product:
        with self.uow:
            self.uow.repository.insert_update({'id': product.id,
                                               'name': product.name,
                                               'category': product.category,
                                               'description': product.description,
                                                  'image': product.image,
                                               'stock': product.stock,
                                               'price': product.price})
            self.uow.commit()
            return product

    def delete_product(self, product_id: str) -> None:
        with self.uow:
            self.uow.repository.delete(product_id)
            self.uow.commit()
