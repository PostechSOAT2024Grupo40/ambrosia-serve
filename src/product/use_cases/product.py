from typing import Dict, Optional, List

from src.product.domain.entities.product import Product
from src.product.domain.validators.product_validator import ProductValidator
from src.product.exceptions import ProductExistsError, ProductNotFoundError
from src.product.ports.product_gateway import IProductGateway


class ProductUseCase:

    @staticmethod
    def create_new_product(request_data: Dict, gateway: IProductGateway):
        product = Product(
            description=request_data['description'],
            category=request_data['category'],
            price=request_data['price'],
            stock=request_data['stock'])

        if ProductUseCase.get_product_by_sku(sku=product.sku, gateway=gateway):
            raise ProductExistsError(product=request_data['description'])

        return gateway.create_update_product(product)

    @staticmethod
    def get_product_by_sku(sku: str, gateway: IProductGateway) -> Optional[Product]:
        return gateway.get_product_by_sku(sku)

    @staticmethod
    def update_product(sku: str, request_data: Dict, gateway: IProductGateway):
        if ProductUseCase.get_product_by_sku(sku=sku, gateway=gateway):
            raise ProductNotFoundError(product=sku)

        product = Product(
            description=request_data['description'],
            category=request_data['category'],
            price=request_data['price'],
            stock=request_data['stock'])

        product.description = request_data['description']
        product.category = request_data['category']
        product.price = request_data['price']
        product.stock = request_data['stock']

        ProductValidator.validate(product=product)

        return gateway.create_update_product(product)

    @staticmethod
    def get_products(gateway: IProductGateway) -> List[Product]:
        return gateway.get_products()

    @staticmethod
    def delete_product(sku: str, gateway: IProductGateway):
        product_ = ProductUseCase.get_product_by_sku(sku=sku, gateway=gateway)
        if product_:
            raise ProductNotFoundError(product=sku)

        gateway.delete_product(sku)
