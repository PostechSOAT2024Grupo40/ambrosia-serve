from typing import Dict

from src.cart.adapters.postgres_gateway import PostgreSqlOrderGateway
from src.cart.adapters.postgresql_uow import CartPostgreSqlUow
from src.cart.adapters.pydantic_presenter import PydanticCartPresenter
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.ports.cart_presenter import ICartPresenter
from src.cart.ports.unit_of_work_interface import ICartUnitOfWork
from src.cart.use_cases.create_cart import CreateCartUseCase
from src.cart.use_cases.delete_order import DeleteOrderUseCase
from src.cart.use_cases.get_all_orders import GetAllOrdersUseCase
from src.cart.use_cases.get_order_by_id import GetOrderByIdUseCase
from src.cart.use_cases.update_order_status import UpdateOrderStatusUseCase
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

        use_case = CreateCartUseCase(cart_gateway=cart_gateway,
                                     user_gateway=user_gateway,
                                     product_gateway=product_gateway,
                                     get_order_by_id=GetOrderByIdUseCase(gateway=cart_gateway))
        order = use_case.execute(request_data=request_data)
        return presenter.present(order)

    @staticmethod
    def get_orders():
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        product_uow: IProductUnitOfWork = ProductPostgreSqlUow(session_factory=postgresql_session_factory())
        product_gateway: IProductGateway = PostgreSqlProductGateway(product_uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        use_case = GetAllOrdersUseCase(gateway=cart_gateway, product_gateway=product_gateway)
        orders = use_case.execute()
        return presenter.present(orders)

    @staticmethod
    def get_order_by_id(order_id: str):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        use_case = GetOrderByIdUseCase(gateway=cart_gateway)
        order = use_case.execute(order_id=order_id)
        return presenter.present(order)

    @staticmethod
    def update_order_status(order_id: str, new_status: str):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        presenter: ICartPresenter = PydanticCartPresenter()
        use_case = UpdateOrderStatusUseCase(gateway=cart_gateway,
                                            get_order_by_id=GetOrderByIdUseCase(gateway=cart_gateway))
        order = use_case.execute(order_id=order_id, new_status=new_status)
        return presenter.present(order)

    @staticmethod
    def delete_order(order_id: str):
        uow: ICartUnitOfWork = CartPostgreSqlUow(session_factory=postgresql_session_factory())
        cart_gateway: ICartGateway = PostgreSqlOrderGateway(uow)
        use_case = DeleteOrderUseCase(gateway=cart_gateway)
        use_case.execute(order_id=order_id)
        return True
