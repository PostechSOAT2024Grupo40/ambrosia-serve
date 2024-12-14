from typing import Dict, Optional, List

from src.product.domain.entities.product import Product
from src.product.domain.validators.product_validator import ProductValidator
from src.product.exceptions import ProductExistsError, ProductNotFoundError
from src.product.ports.product_gateway import IProductGateway


class ProductUseCase:

    @staticmethod
    def create_new_product(request_data: Dict, gateway: IProductGateway):
        if ProductUseCase.get_product_by_name(request_data['name'], gateway):
            raise ProductExistsError(f"Produto {request_data['name']} ja existe")

        product = Product(
            name=request_data['name'],
            description=request_data['description'],
            category=request_data['category'],
            price=request_data['price'],
            stock=request_data['stock'])

        return gateway.create_update_product(product)

    @staticmethod
    def get_product_by_id(product_id: str, gateway: IProductGateway) -> Optional[Product]:
        return gateway.get_product_by_id(product_id=product_id)

    @staticmethod
    def update_product(product_id: str, request_data: Dict, gateway: IProductGateway):
        if not ProductUseCase.get_product_by_id(product_id=product_id, gateway=gateway):
            raise ProductNotFoundError(product=product_id)

        product = Product(
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

        return gateway.create_update_product(product)

    @staticmethod
    def get_products(gateway: IProductGateway) -> List[Product]:
        return gateway.get_products()

    @staticmethod
    def delete_product(product_id: str, gateway: IProductGateway):
        product_ = ProductUseCase.get_product_by_id(product_id=product_id, gateway=gateway)
        if not product_:
            raise ProductNotFoundError(product=product_id)

        gateway.delete_product(product_id)

    @staticmethod
    def get_product_by_name(product_name: str, gateway: IProductGateway) -> Optional[Product]:
        return gateway.get_product_by_name(product_name=product_name)
