from typing import Dict

from src.cart.ports.cart_gateway import ICartGateway


class CartUseCase:

    @staticmethod
    def create_new_order(request_data: Dict, gateway: ICartGateway):
        pass

    @staticmethod
    def get_all_orders(gateway: ICartGateway):
        pass

    @staticmethod
    def get_order_by_id(order_id: str, gateway: ICartGateway):
        pass

    @staticmethod
    def update_order(order_id: str, request_data: Dict, gateway: ICartGateway):
        pass

    @staticmethod
    def delete_order(order_id: str, gateway: ICartGateway):
        pass
