from typing import Dict

from src.product.adapters.postgres_gateway import PostgreSqlProductGateway
from src.product.adapters.postgresql_uow import PostgreSqlUow
from src.product.adapters.pydantic_presenter import PydanticProductPresenter
from src.product.ports.product_gateway import IProductGateway
from src.product.ports.product_presenter import IProductPresenter
from src.product.ports.unit_of_work_interface import IProductUnitOfWork
from src.product.use_cases.product import ProductUseCase
from src.shared.postgresql_session_factory import postgresql_session_factory


class ProductController:

    @staticmethod
    def create_product(request_data: Dict):
        uow: IProductUnitOfWork = PostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        product = ProductUseCase.create_new_product(request_data=request_data, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def get_products():
        uow: IProductUnitOfWork = PostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        products = ProductUseCase.get_products(gateway=gateway)
        return presenter.present(products)

    @staticmethod
    def get_product_by_id(sku: str):
        uow: IProductUnitOfWork = PostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        product = ProductUseCase.get_product_by_sku(sku=sku, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def update_product(sku: str, request_data: Dict):
        uow: IProductUnitOfWork = PostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        product = ProductUseCase.update_product(sku=sku, request_data=request_data, gateway=gateway)
        return presenter.present(product)

    @staticmethod
    def delete_product(sku: str):
        uow: IProductUnitOfWork = PostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        ProductUseCase.delete_product(sku=sku, gateway=gateway)
        return True
