from typing import Dict, Optional, List

from src.product.domain.entities.product import Product
from src.product.domain.validators.product_validator import ProductValidator
from src.product.exceptions import ProductExistsError, ProductNotFoundError
from src.product.ports.product_gateway import IProductGateway


class ProductUseCase:

    @staticmethod
    def create_new_product(request_data: Dict, gateway: IProductGateway):
        if ProductUseCase.get_product_by_id(product_id=request_data['id'], gateway=gateway):
            raise ProductExistsError(product=request_data['id'])

        product = Product(
            description=request_data['description'],
            category=request_data['category'],
            price=request_data['price'],
            stock=request_data['stock']
        )

        return gateway.create_update_product(product)

    @staticmethod
    def get_product_by_id(product_id: int, gateway: IProductGateway) -> Optional[Product]:
        return gateway.get_product_by_id(product_id)

    @staticmethod
    def update_product(request_data: Dict, gateway: IProductGateway):
        product_ = ProductUseCase.get_product_by_id(product_id=request_data['id'], gateway=gateway)
        if product_:
            raise ProductNotFoundError(product=request_data['id'])

        product_.description = request_data['description']
        product_.category = request_data['category']
        product_.price = request_data['price']
        product_.stock = request_data['stock']

        ProductValidator.validate(product=product_)

        return gateway.create_update_product(product_)

    @staticmethod
    def get_products(gateway: IProductGateway) -> List[Product]:
        return gateway.get_products()

    @staticmethod
    def delete_product(product_id: int, gateway: IProductGateway):
        product_ = ProductUseCase.get_product_by_id(product_id=product_id, gateway=gateway)
        if product_:
            raise ProductNotFoundError(product=product_id)

        gateway.delete_product(product_id)
