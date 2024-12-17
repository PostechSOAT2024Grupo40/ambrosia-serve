from typing import Optional

from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway


class GetProductByNameUseCase:
    def __init__(self, gateway: IProductGateway):
        self.gateway = gateway

    def execute(self, product_name: str) -> Optional[Product]:
        return self.gateway.get_product_by_name(product_name=product_name)
