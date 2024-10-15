from typing import List

from src.cart.domain.entities.order import Order
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.ports.unit_of_work_interface import ICartUnitOfWork


class PostgreSqlOrderGateway(ICartGateway):

    def __init__(self, uow: ICartUnitOfWork):
        super().__init__()
        self.uow = uow

    def get_orders(self) -> List[Order]:
        with self.uow:
            orders = self.uow.repository.get_all()
            return [Order(**o) for o in orders]

    def get_order_by_id(self, order_id: str) -> Order:
        with self.uow:
            order = self.uow.repository.filter_by_id(order_id)
            return Order(**order)

    def create_update_order(self, order: Order) -> Order:
        with self.uow:
            self.uow.repository.insert_update({
                'id': order.id,
                'user_id': order.user,
                'order_status': order.order_status,
                'payment_condition': order.payment_condition,
                'products': [{'id': p.id,
                              'product': p.product.id,
                              'quantity': p.quantity,
                              'observation': p.observation} for p in order.products]
            })
            self.uow.commit()
            return order

    def delete_order(self, order_id: str) -> None:
        with self.uow:
            self.uow.repository.delete(order_id)
            self.uow.commit()
