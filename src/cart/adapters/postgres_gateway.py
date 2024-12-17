from typing import Optional

from sqlalchemy import Row

from src.cart.domain.entities.order import Order
from src.cart.domain.enums.paymentConditions import PaymentConditions
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.ports.unit_of_work_interface import ICartUnitOfWork


class PostgreSqlOrderGateway(ICartGateway):

    def __init__(self, uow: ICartUnitOfWork):
        super().__init__()
        self.uow = uow

    def get_order_products(self, order_id) -> list[dict]:
        with self.uow:
            order_products: list[Row] = self.uow.repository.get_order_products(order_id)
            return [{
                'id': p.id,
                'product_id': p.product_id,
                'quantity': p.quantity,
                'observation': p.observation
            } for p in order_products]

    def get_orders(self) -> list[Order]:
        with self.uow:
            orders: Optional[list[Row]] = self.uow.repository.get_all()
            return [self.build_order_entity(o) for o in orders]

    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        with self.uow:
            order = self.uow.repository.filter_by_id(order_id)
            if not order:
                return
            return self.build_order_entity(order)

    def create_update_order(self, order: Order) -> Order:
        with self.uow:
            condition = PaymentConditions(order.payment_condition)
            self.uow.repository.insert_update({
                'id': order.id,
                'user_id': order.user,
                'status': order.order_status.value,
                'payment_condition': condition.name,
                'total': order.total_order,
                'products': [{'id': p.id,
                              'product_id': p.product.id,
                              'quantity': p.quantity,
                              'observation': p.observation} for p in order.products]
            })
            self.uow.commit()
            return order

    def delete_order(self, order_id: str) -> None:
        with self.uow:
            self.uow.repository.delete(order_id)
            self.uow.commit()

    @staticmethod
    def build_order_entity(order):
        if not order:
            return None

        payment_condition = PaymentConditions[order.payment_condition]

        return Order(_id=order.id,
                     user=order.user_id,
                     order_datetime=order.created_at,
                     order_status=order.status,
                     payment_condition=payment_condition.value)
