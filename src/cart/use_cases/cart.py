from datetime import datetime
from typing import Dict, List

from src.cart.domain.entities.order import Order
from src.cart.domain.entities.order_product import OrderProduct
from src.cart.domain.enums.order_status import OrderStatus
from src.cart.domain.validators.order_validator import OrderValidator
from src.cart.exceptions import (ClientError,
                                 ProductNotFoundError,
                                 OrderExistsError,
                                 OrderNotFoundError)
from src.cart.ports.cart_gateway import ICartGateway
from src.client.ports.user_gateway import IUserGateway
from src.product.ports.product_gateway import IProductGateway


class CartUseCase:

    @staticmethod
    def create_new_order(request_data: Dict,
                         cart_gateway: ICartGateway,
                         user_gateway: IUserGateway,
                         product_gateway: IProductGateway):
        user_id = request_data['user_id']
        if not user_gateway.get_user_by_id(user_id):
            raise ClientError(client=user_id)
        products_required = CartUseCase.build_products_required_list(product_gateway, request_data['products'])

        order = Order(user=user_id,
                      order_datetime=datetime.now(),
                      order_status=OrderStatus.PENDENTE,
                      payment_condition=request_data['payment_condition'],
                      products=products_required)
        if CartUseCase.get_order_by_id(order.id, cart_gateway):
            raise OrderExistsError(order=order.id)

        return cart_gateway.create_update_order(order)

    @staticmethod
    def build_products_required_list(product_gateway: IProductGateway, products: List[Dict]):
        products_required = []
        for product_required in products:
            sku = product_required['product_sku']
            product_entity = product_gateway.get_product_by_sku(sku)
            if not product_entity:
                raise ProductNotFoundError(product=sku)

            order_product = OrderProduct(product=product_entity,
                                         quantity=product_required['quantity'],
                                         observation=product_required.get('observation', ''))
            product_entity.stock -= order_product.quantity if product_entity.stock - order_product.quantity > 0 else 0
            product_gateway.create_update_product(product=product_entity)

            products_required.append(order_product)
        return products_required

    @staticmethod
    def get_all_orders(gateway: ICartGateway):
        return gateway.get_orders()

    @staticmethod
    def get_order_by_id(order_id: str, gateway: ICartGateway):
        return gateway.get_order_by_id(order_id=order_id)

    @staticmethod
    def delete_order(order_id: str, gateway: ICartGateway):
        gateway.delete_order(order_id=order_id)

    @staticmethod
    def update_order_status(order_id: str, new_status: str, gateway: ICartGateway):
        order = CartUseCase.get_order_by_id(order_id, gateway)
        if not order:
            raise OrderNotFoundError(order=order_id)
        order.order_status = new_status
        OrderValidator.validate(order)
        return gateway.create_update_order(order)
