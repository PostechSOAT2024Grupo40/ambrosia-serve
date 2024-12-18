from datetime import datetime
from typing import Dict

from src.cart.domain.entities.order import Order
from src.cart.domain.entities.order_product import OrderProduct
from src.cart.domain.enums.order_status import OrderStatus
from src.cart.exceptions import (ClientError,
                                 ProductNotFoundError,
                                 OrderExistsError, OrderNotFoundError)
from src.cart.ports.cart_gateway import ICartGateway
from src.cart.use_cases.get_order_by_id import GetOrderByIdUseCase
from src.client.ports.user_gateway import IUserGateway
from src.product.ports.product_gateway import IProductGateway


class CreateCartUseCase:
    def __init__(self, cart_gateway: ICartGateway,
                 user_gateway: IUserGateway,
                 product_gateway: IProductGateway,
                 get_order_by_id: GetOrderByIdUseCase):
        self.cart_gateway = cart_gateway
        self.user_gateway = user_gateway
        self.product_gateway = product_gateway
        self.get_order_by_id = get_order_by_id

    def execute(self, request_data: Dict):
        user_id = request_data['user_id']
        if not self.user_gateway.get_user_by_id(user_id):
            raise ClientError(client=user_id)
        products_required = self.build_products_required_list(request_data['products'])

        order = Order(user=user_id,
                      order_datetime=datetime.now(),
                      order_status=OrderStatus.PENDENTE,
                      payment_condition=request_data['payment_condition'])

        for product in products_required:
            order.add_product(product)
        try:
            if self.get_order_by_id.execute(order.id):
                raise OrderExistsError(order=order.id)
        except OrderNotFoundError:
            pass

        return self.cart_gateway.create_update_order(order)

    def build_products_required_list(self, products: list[Dict]):
        products_required = []
        for product_required in products:
            product_id = product_required['product_id']
            product_entity = self.product_gateway.get_product_by_id(product_id)
            if not product_entity:
                raise ProductNotFoundError(product=product_id)

            order_product = OrderProduct(product=product_entity,
                                         quantity=product_required['quantity'],
                                         observation=product_required.get('observation', ''))
            product_entity.stock -= order_product.quantity if product_entity.stock - order_product.quantity > 0 else 0
            self.product_gateway.create_update_product(product=product_entity)

            products_required.append(order_product)
        return products_required
