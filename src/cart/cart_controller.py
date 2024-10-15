from typing import Dict

from src.cart.adapters.postgres_gateway import PostgreSqlOrderGateway
from src.cart.adapters.postgresql_uow import CartPostgreSqlUow
from src.cart.adapters.pydantic_presenter import PydanticCartPresenter
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.ports.cart_presenter import ICartPresenter
from src.cart.ports.unit_of_work_interface import ICartUnitOfWork
from src.cart.use_cases.cart import CartUseCase
from src.client.adapters.postgres_gateway import PostgreSqlClientGateway
from src.client.adapters.postgresql_uow import ClientPostgreSqlUow
from src.client.ports.unit_of_work_interface import IClientUnitOfWork
from src.client.ports.user_gateway import IUserGateway
from src.product.adapters.postgres_gateway import PostgreSqlProductGateway
from src.product.adapters.postgresql_uow import ProductPostgreSqlUow
from src.product.ports.product_gateway import IProductGateway
from src.product.ports.unit_of_work_interface import IProductUnitOfWork
from src.shared.postgresql_session_factory import postgresql_session_factory


class CartController:

    @staticmethod
    def create_order(request_data: Dict):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        user_uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        user_gateway: IUserGateway = PostgreSqlClientGateway(user_uow)
        product_uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        product_gateway: IProductGateway = PostgreSqlProductGateway(product_uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        order = CartUseCase.create_new_order(request_data=request_data,
                                             cart_gateway=cart_gateway,
                                             user_gateway=user_gateway,
                                             product_gateway=product_gateway)
        return presenter.present(order)

    @staticmethod
    def get_orders():
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        orders = CartUseCase.get_all_orders(gateway=cart_gateway)
        return presenter.present(orders)

    @staticmethod
    def get_order_by_id(order_id: str):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        order = CartUseCase.get_order_by_id(order_id=order_id, gateway=cart_gateway)
        return presenter.present(order)

    @staticmethod
    def update_order(order_id: str, request_data: Dict):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        product_uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        product_gateway: IProductGateway = PostgreSqlProductGateway(product_uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        order = CartUseCase.update_order(order_id=order_id,
                                         request_data=request_data,
                                         gateway=cart_gateway,
                                         product_gateway=product_gateway)
        return presenter.present(order)

    @staticmethod
    def update_order_status(order_id: str, new_status: str):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        order = CartUseCase.update_order_status(order_id=order_id,
                                                new_status=new_status,
                                                gateway=cart_gateway)
        return presenter.present(order)

    @staticmethod
    def delete_order(order_id: str):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        CartUseCase.delete_order(order_id=order_id, gateway=cart_gateway)
        return True
