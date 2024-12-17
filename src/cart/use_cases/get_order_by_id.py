from src.cart.ports.cart_gateway import ICartGateway


class GetOrderByIdUseCase:
    def __init__(self, gateway: ICartGateway):
        self.gateway = gateway

    def execute(self, order_id: str):
        return self.gateway.get_order_by_id(order_id=order_id)
