
from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway


class GetAllProductsUseCase:
    def __init__(self, gateway: IProductGateway):
        self.gateway = gateway

    def execute(self) -> list[Product]:
        return self.gateway.get_products()
