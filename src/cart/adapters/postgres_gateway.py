from typing import List

from src.cart.domain.entities.order import Order
from src.cart.domain.entities.order_product import OrderProduct
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.ports.unit_of_work_interface import ICartUnitOfWork


class PostgreSqlOrderGateway(ICartGateway):

    def __init__(self, uow: ICartUnitOfWork):
        super().__init__()
        self.uow = uow

    def get_orders(self) -> List[Order]:
        with self.uow:
            orders = self.uow.repository.get_all()
            return [self.build_order_entity(o) for o in orders]

    def get_order_by_id(self, order_id: str) -> Order:
        with self.uow:
            order = self.uow.repository.filter_by_id(order_id)
            return self.build_order_entity(order)

    def create_update_order(self, order: Order) -> Order:
        with self.uow:
            self.uow.repository.insert_update({
                'id': order.id,
                'user_id': order.user,
                'order_status': order.order_status,
                'payment_condition': order.payment_condition,
                'products': [{'id': p.id,
                              'product': p.product, # sku
                              'quantity': p.quantity,
                              'observation': p.observation} for p in order.products]
            })
            self.uow.commit()
            return order

    def delete_order(self, order_id: str) -> None:
        with self.uow:
            self.uow.repository.delete(order_id)
            self.uow.commit()

    def build_order_entity(self, order):
        products = [self.build_order_product_entity(p) for p in order['products']]

        return Order(_id=order['id'],
                     user=order['user_id'],
                     order_datetime=order['order_datetime'],
                     order_status=order['order_status'],
                     payment_condition=order['payment_condition'],
                     products=products)

    @staticmethod
    def build_order_product_entity(product):
        return OrderProduct(_id=product['id'],
                            product=product['product'], # sku
                            quantity=product['quantity'],
                            observation=product.get('observation', ''))
