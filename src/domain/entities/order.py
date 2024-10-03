import uuid
from datetime import datetime
from typing import List

from src.domain.domain_exception import DomainException
from src.domain.enums.order_status import OrderStatus
from src.domain.enums.paymentConditions import PaymentConditions


class Order:
    def __init__(self,
                 user: int,
                 user_address: int,
                 total_order: float,
                 delivery_value: float,
                 product_quantity: int,
                 order_datetime: datetime,
                 order_status: OrderStatus,
                 payment_condition: PaymentConditions,
                 order_items: List = None):
        self.id = str(uuid.uuid4())
        self.user = user
        self.user_address = user_address
        self.total_order = total_order
        self.delivery_value = delivery_value
        self.product_quantity = product_quantity
        self.order_datetime = order_datetime
        self.order_status = order_status
        self.payment_condition = payment_condition
        self.order_items = order_items if order_items is not None else []

        self.__validator()

    def __validator(self):
        self.__validate_payment_condition()
        self.__validate_order_status()
        self.__validate_total_price()
        self.__validate_delivery_value()
        self.__validate_order_items()

    def __validate_payment_condition(self):
        try:
            PaymentConditions(self.payment_condition)
        except ValueError:
            raise DomainException("Forma de Pagamento inválida")

    def __validate_order_status(self):
        try:
            OrderStatus(self.order_status)
        except ValueError:
            raise DomainException("Status do Pedido inválido")

    def __validate_total_price(self):
        if self.total_order <= 0:
            raise DomainException("O valor total não pode ser menor ou igual a zero")

    def __validate_delivery_value(self):
        if self.delivery_value < 0:
            raise DomainException("O valor de entrega não pode ser negativo")

    def __validate_order_items(self):
        if self.product_quantity <= 0:
            raise DomainException("A quantidade de produtos não pode ser menor ou igual a zero")
