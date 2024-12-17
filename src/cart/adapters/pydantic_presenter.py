
from src.api.presentation.shared.dtos.order_response_dto import OrderResponseDto, OrderProductResponseDto
from src.cart.domain.entities.order import Order
from src.cart.domain.enums.order_status import OrderStatus
from src.cart.ports.cart_presenter import ICartPresenter


class PydanticCartPresenter(ICartPresenter):

    def present(self, output: Order | list[Order]) -> OrderResponseDto | list[OrderResponseDto]:
        if isinstance(output, list):
            return [self.formater(order) for order in output]
        return self.formater(output)

    @staticmethod
    def formater(order):
        if not order:
            return {}

        return OrderResponseDto(id=order.id,
                                user=order.user,
                                total_order=order.total_order,
                                order_status=OrderStatus(order.order_status),
                                payment_condition=order.payment_condition,
                                products=[OrderProductResponseDto(
                                    product=p.product.id,
                                    quantity=p.quantity,
                                    observation=p.observation
                                ) for p in order.products])
