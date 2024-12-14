from typing import Dict

from src.product.adapters.postgres_gateway import PostgreSqlProductGateway
from src.product.adapters.postgresql_uow import ProductPostgreSqlUow
from src.product.adapters.pydantic_presenter import PydanticProductPresenter
from src.product.ports.product_gateway import IProductGateway
from src.product.ports.product_presenter import IProductPresenter
from src.product.ports.unit_of_work_interface import IProductUnitOfWork
from src.product.use_cases.create_product import CreateProductUseCase
from src.product.use_cases.delete_product import DeleteProductUseCase
from src.product.use_cases.get_all_products import GetAllProductsUseCase
from src.product.use_cases.get_product_by_id import GetProductByIdUseCase
from src.product.use_cases.update_product import UpdateProductUseCase
from src.shared.postgresql_session_factory import postgresql_session_factory


class ProductController:

    @staticmethod
    def create_product(request_data: Dict):
        uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        create_product_usecase = CreateProductUseCase(gateway=gateway)
        product = create_product_usecase.execute(request_data=request_data)
        return presenter.present(product)

    @staticmethod
    def get_products():
        uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        get_all_products_usecase = GetAllProductsUseCase(gateway=gateway)
        products = get_all_products_usecase.execute()
        return presenter.present(products)

    @staticmethod
    def get_product_by_id(product_id: str):
        uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        get_product_by_id = GetProductByIdUseCase(gateway=gateway)
        product = get_product_by_id.execute(product_id=product_id)
        return presenter.present(product)

    @staticmethod
    def update_product(product_id: str, request_data: Dict):
        uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        presenter: IProductPresenter = PydanticProductPresenter()
        update_product_usecase = UpdateProductUseCase(gateway=gateway)
        product = update_product_usecase.execute(product_id=product_id, request_data=request_data)
        return presenter.present(product)

    @staticmethod
    def delete_product(product_id: str):
        uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IProductGateway = PostgreSqlProductGateway(uow)
        delete_product_usecase = DeleteProductUseCase(gateway=gateway)
        delete_product_usecase.execute(product_id=product_id)
        return True
