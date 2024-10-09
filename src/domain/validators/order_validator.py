from src.domain.domain_exception import DomainException
from src.domain.enums.order_status import OrderStatus
from src.domain.enums.paymentConditions import PaymentConditions


class OrderValidator:
    @staticmethod
    def validate(order):
        OrderValidator._validate_payment_condition(order)
        OrderValidator.__validate_order_status(order)
        OrderValidator.__validate_total_price(order)
        OrderValidator.__validate_delivery_value(order)
        OrderValidator.__validate_order_items(order)

    @staticmethod
    def _validate_payment_condition(order):
        try:
            PaymentConditions(order.payment_condition)
        except ValueError:
            raise DomainException("Forma de Pagamento inválida")

    @staticmethod
    def __validate_order_status(order):
        try:
            OrderStatus(order.order_status)
        except ValueError:
            raise DomainException("Status do Pedido inválido")

    @staticmethod
    def __validate_total_price(order):
        if order.total_order <= 0:
            raise DomainException("O valor total não pode ser menor ou igual a zero")

    @staticmethod
    def __validate_delivery_value(order):
        if order.delivery_value < 0:
            raise DomainException("O valor de entrega não pode ser negativo")

    @staticmethod
    def __validate_order_items(order):
        if order.product_quantity <= 0:
            raise DomainException("A quantidade de produtos não pode ser menor ou igual a zero")
