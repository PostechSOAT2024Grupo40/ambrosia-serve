from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway


class MockProductGateway(IProductGateway):
    def __init__(self):
        self.products_by_id: dict[str, Product] = {}

    def get_products(self) -> list[Product]:
        return list(self.products_by_id.values())

    def get_product_by_id(self, product_id: str) -> Product:
        return self.products_by_id.get(product_id)

    def create_update_product(self, product: Product) -> Product:
        self.products_by_id[product.id] = product
        return product

    def delete_product(self, product_id: str) -> None:
        self.products_by_id.pop(product_id, None)

    def get_product_by_name(self, product_name: str):
        return next((product for product in self.products_by_id.values() if product.name == product_name), None)
