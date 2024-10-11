from typing import Dict

from src.product.adapters.in_memory_product_gateway import InMemoryProductGateway
from src.product.adapters.in_memory_repository import InMemoryRepository
from src.product.adapters.in_memory_uow import InMemoryUow
from src.product.adapters.json_presenter import JsonProductPresenter
from src.product.ports.product_gateway import IProductGateway
from src.product.ports.product_presenter import IProductPresenter
from src.product.ports.repository_interface import IRepository
from src.product.ports.unit_of_work_interface import IProductUnitOfWork
from src.product.use_cases.product import ProductUseCase


class ProductController:

    @staticmethod
    def create_product(request_data: Dict):
        repository: IRepository = InMemoryRepository()
        uow: IProductUnitOfWork = InMemoryUow(repository=repository)
        gateway: IProductGateway = InMemoryProductGateway(uow=uow)
        presenter: IProductPresenter = JsonProductPresenter()
        product = ProductUseCase.create_new_product(request_data=request_data, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def get_products():
        repository: IRepository = InMemoryRepository()
        uow: IProductUnitOfWork = InMemoryUow(repository=repository)
        gateway: IProductGateway = InMemoryProductGateway(uow=uow)
        presenter: IProductPresenter = JsonProductPresenter()
        products = ProductUseCase.get_products(gateway=gateway)
        return presenter.present(products)

    @staticmethod
    def get_product_by_id(sku: str):
        repository: IRepository = InMemoryRepository()
        uow: IProductUnitOfWork = InMemoryUow(repository=repository)
        gateway: IProductGateway = InMemoryProductGateway(uow=uow)
        presenter: IProductPresenter = JsonProductPresenter()
        product = ProductUseCase.get_product_by_sku(sku=sku, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def update_product(sku:str, request_data: Dict):
        repository: IRepository = InMemoryRepository()
        uow: IProductUnitOfWork = InMemoryUow(repository=repository)
        gateway: IProductGateway = InMemoryProductGateway(uow=uow)
        presenter: IProductPresenter = JsonProductPresenter()
        product = ProductUseCase.update_product(sku=sku, request_data=request_data, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def delete_product(sku: str):
        repository: IRepository = InMemoryRepository()
        uow: IProductUnitOfWork = InMemoryUow(repository=repository)
        gateway: IProductGateway = InMemoryProductGateway(uow=uow)
        ProductUseCase.delete_product(sku=sku, gateway=gateway)
        return True
