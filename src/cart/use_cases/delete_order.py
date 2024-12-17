from src.cart.ports.cart_gateway import ICartGateway


class DeleteOrderUseCase:
    def __init__(self, gateway: ICartGateway):
        self.gateway = gateway

    def execute(self, order_id: str):
        return self.gateway.delete_order(order_id=order_id)
