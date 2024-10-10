from typing import Dict

from src.product.ports.product_gateway import IProductGateway
from src.product.ports.product_presenter import IProductPresenter
from src.product.use_cases.product import ProductUseCase
from src.shared.repository_interface import IRepository


class ProductController:

    @staticmethod
    def create_product(request_data: Dict):
        repository: IRepository = ...
        gateway: IProductGateway = ...
        presenter: IProductPresenter = ...
        product = ProductUseCase.create_new_product(request_data=request_data, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def get_products():
        repository: IRepository = ...
        gateway: IProductGateway = ...
        presenter: IProductPresenter = ...
        products = ProductUseCase.get_products(gateway=gateway)
        return presenter.present(products)

    @staticmethod
    def get_product_by_id(product_id: int):
        repository: IRepository = ...
        gateway: IProductGateway = ...
        presenter: IProductPresenter = ...
        product = ProductUseCase.get_product_by_id(product_id=product_id, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def update_product(request_data: Dict):
        repository: IRepository = ...
        gateway: IProductGateway = ...
        presenter: IProductPresenter = ...
        product = ProductUseCase.update_product(request_data=request_data, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def delete_product(product_id: int):
        repository: IRepository = ...
        gateway: IProductGateway = ...
        ProductUseCase.delete_product(product_id=product_id, gateway=gateway)
        return True
