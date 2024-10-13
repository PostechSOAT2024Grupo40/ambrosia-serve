from datetime import datetime
from typing import List

from src.cart.domain.enums.order_status import OrderStatus
from src.cart.domain.enums.paymentConditions import PaymentConditions
from src.cart.domain.object_values import generate_id
from src.cart.domain.validators.order_validator import OrderValidator
from src.product.domain.entities.product import Product


class Order:
    def __init__(self,
                 user: int,
                 total_order: float,
                 product_quantity: int,
                 order_datetime: datetime,
                 order_status: OrderStatus,
                 payment_condition: PaymentConditions,
                 _order_items: List[Product],
                 _id: str = generate_id()):
        self._id = _id
        self.user = user
        self.total_order = total_order
        self.product_quantity = product_quantity
        self.order_datetime = order_datetime
        self.order_status = order_status
        self.payment_condition = payment_condition
        self._order_items = _order_items

        OrderValidator.validate(order=self)
        OrderValidator.validate_order_items(order_items=_order_items)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self):
        return self._id

    @property
    def order_items(self):
        return self._order_items
