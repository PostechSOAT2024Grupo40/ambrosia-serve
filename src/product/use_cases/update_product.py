from typing import Dict

from src.product.domain.entities.product import Product
from src.product.domain.validators.product_validator import ProductValidator
from src.product.exceptions import ProductNotFoundError
from src.product.ports.product_gateway import IProductGateway


class UpdateProductUseCase:
    def __init__(self, gateway: IProductGateway):
        self.gateway = gateway

    def execute(self, product_id: str, request_data: Dict):
        if not self.gateway.get_product_by_id(product_id=product_id):
            raise ProductNotFoundError(product=product_id)

        product = Product(
            _id=product_id,
            name=request_data['name'],
            description=request_data['description'],
            category=request_data['category'],
            price=request_data['price'],
            stock=request_data['stock'])

        product.description = request_data['description']
        product.category = request_data['category']
        product.price = request_data['price']
        product.stock = request_data['stock']

        ProductValidator.validate(product=product)

        return self.gateway.create_update_product(product)
