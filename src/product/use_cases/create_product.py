from typing import Dict

from src.product.domain.entities.product import Product
from src.product.exceptions import ProductExistsError
from src.product.ports.product_gateway import IProductGateway


class CreateProductUseCase:
    def __init__(self, gateway: IProductGateway):
        self.gateway = gateway

    def execute(self, request_data: Dict):
        if self.gateway.get_product_by_name(request_data['name']):
            raise ProductExistsError(f"Produto {request_data['name']} ja existe")

        product = Product(
            name=request_data['name'],
            description=request_data['description'],
            category=request_data['category'],
            price=request_data['price'],
            stock=request_data['stock'])

        return self.gateway.create_update_product(product)
