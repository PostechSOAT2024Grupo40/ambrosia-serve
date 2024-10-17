from typing import List

from src.cart.domain.entities.order import Order
from src.cart.domain.entities.order_product import OrderProduct
from src.cart.domain.enums.paymentConditions import PaymentConditions
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.ports.unit_of_work_interface import ICartUnitOfWork
from src.product.domain.entities.product import Product


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
            condition = PaymentConditions(order.payment_condition)
            self.uow.repository.insert_update({
                'id': order.id,
                'user_id': order.user,
                'status': order.order_status.value,
                'payment_condition': condition.name,
                'products': [{'id': p.id,
                              'product_id': p.product.sku,  # sku
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
        payment_condition = PaymentConditions[order['payment_condition']]
        products = []
        for p in order['products']:
            products.append(
                OrderProduct(
                    product=Product(_id=p['id'],
                                    sku=p['sku'],
                                    description=p['description'],
                                    category=p['category'],
                                    stock=p['stock'],
                                    price=p['price']),
                    quantity=p['quantity'],
                    observation=p['observation']
                )
            )
        return Order(_id=order['id'],
                     user=order['user_id'],
                     order_datetime=order['created_at'],
                     order_status=order['status'],
                     payment_condition=payment_condition.value,
                     products=products)
