from src.cart.domain.domain_exception import OrderDomainException
from src.cart.domain.enums.order_status import OrderStatus
from src.cart.domain.enums.paymentConditions import PaymentConditions


class OrderValidator:
    @staticmethod
    def validate(order):
        OrderValidator._validate_payment_condition(order)
        OrderValidator.__validate_order_status(order)

    @staticmethod
    def _validate_payment_condition(order):
        try:
            PaymentConditions(order.payment_condition)
        except ValueError:
            raise OrderDomainException("Forma de Pagamento inválida")

    @staticmethod
    def __validate_order_status(order):
        try:
            OrderStatus(order.order_status)
        except ValueError:
            raise OrderDomainException("Status do Pedido inválido")
