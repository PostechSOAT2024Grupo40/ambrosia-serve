from datetime import datetime
from typing import List

from src.cart.domain.entities.order_product import OrderProduct
from src.cart.domain.enums.order_status import OrderStatus
from src.cart.domain.enums.paymentConditions import PaymentConditions
from src.cart.domain.object_values import generate_id
from src.cart.domain.validators.order_validator import OrderValidator


class Order:
    def __init__(self,
                 user: int,
                 order_datetime: datetime,
                 order_status: OrderStatus,
                 payment_condition: PaymentConditions,
                 _id: str = generate_id()):
        self._id = _id
        self.user = user
        self._total_order = 0.0
        self.order_datetime = order_datetime
        self.order_status = order_status
        self.payment_condition = payment_condition
        self.products: List[OrderProduct] = []

        OrderValidator.validate(order=self)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self):
        return self._id

    def add_product(self, product: OrderProduct):
        self.products.append(product)

    @property
    def total_order(self):
        return sum(self.calculate_total_price_per_quantity(order_item) for order_item in self.products)

    @staticmethod
    def calculate_total_price_per_quantity(order_item):
        return order_item.product.price * order_item.quantity
