from typing import Dict

from src.cart.ports.cart_gateway import ICartGateway
from src.cart.ports.cart_presenter import ICartPresenter
from src.cart.ports.repository_interface import IRepository
from src.cart.use_cases.cart import CartUseCase


class CartController:

    @staticmethod
    def create_order(request_data: Dict):
        repository: IRepository = ...
        gateway: ICartGateway = ...
        presenter: ICartPresenter = ...
        order = CartUseCase.create_new_order(request_data=request_data, gateway=gateway)
        return presenter.present(order)

    @staticmethod
    def get_orders():
        repository: IRepository = ...
        gateway: ICartGateway = ...
        presenter: ICartPresenter = ...
        orders = CartUseCase.get_all_orders(gateway=gateway)
        return presenter.present(orders)

    @staticmethod
    def get_order_by_id(order_id: str):
        repository: IRepository = ...
        gateway: ICartGateway = ...
        presenter: ICartPresenter = ...
        order = CartUseCase.get_order_by_id(order_id=order_id, gateway=gateway)
        return presenter.present(order)

    @staticmethod
    def update_order(order_id: str, request_data: Dict):
        repository: IRepository = ...
        gateway: ICartGateway = ...
        presenter: ICartPresenter = ...
        order = CartUseCase.update_order(order_id=order_id, request_data=request_data, gateway=gateway)
        return presenter.present(order)

    @staticmethod
    def delete_order(order_id: str):
        repository: IRepository = ...
        gateway: ICartGateway = ...
        CartUseCase.delete_order(order_id=order_id, gateway=gateway)
        return True
