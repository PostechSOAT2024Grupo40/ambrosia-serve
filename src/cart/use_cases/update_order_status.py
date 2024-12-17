from src.cart.domain.validators.order_validator import OrderValidator
from src.cart.exceptions import OrderNotFoundError
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.use_cases.get_order_by_id import GetOrderByIdUseCase


class UpdateOrderStatusUseCase:
    def __init__(self, gateway: ICartGateway, get_order_by_id: GetOrderByIdUseCase):
        self.gateway = gateway
        self.get_order_by_id = get_order_by_id

    def execute(self, order_id: str, new_status: str):
        order = self.get_order_by_id.execute(order_id)
        if not order:
            raise OrderNotFoundError(order=order_id)
        order.order_status = new_status
        OrderValidator.validate(order)
        return self.gateway.create_update_order(order)
