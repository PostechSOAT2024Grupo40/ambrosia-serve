import uuid
from datetime import datetime
from typing import List

from src.domain.entities.user import User
from src.domain.enums.order_status import OrderStatus
from src.domain.enums.paymentConditions import PaymentConditions
from src.domain.validators.order_validator import OrderValidator


class Order:
    def __init__(self,
                 user: User,
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

        OrderValidator.validate(order=self)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
