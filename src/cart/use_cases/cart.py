from datetime import datetime
from typing import Dict, Any

from src.cart.domain.entities.order import Order
from src.cart.domain.entities.order_product import OrderProduct
from src.cart.domain.enums.order_status import OrderStatus
from src.cart.domain.validators.order_product_validator import OrderProductValidator
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
        products_required = CartUseCase.build_products_required_list(product_gateway, request_data)

        order = Order(user=user_id,
                      order_datetime=datetime.now(),
                      order_status=OrderStatus.PENDENTE,
                      payment_condition=request_data['payment_condition'],
                      products=products_required)
        if CartUseCase.get_order_by_id(order.id, cart_gateway):
            raise OrderExistsError(order=order.id)

        return cart_gateway.create_update_order(order)

    @staticmethod
    def build_products_required_list(product_gateway: IProductGateway, request_data: Dict):
        products_required = []
        for product_required in request_data['products']:
            sku = product_required['sku']
            product_entity = product_gateway.get_product_by_sku(sku)
            if not product_entity:
                raise ProductNotFoundError(product=sku)

            order_product = OrderProduct(product=product_entity,
                                         quantity=product_required['quantity'],
                                         observation=product_required.get('observation'))
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
    def update_order(order_id: str,
                     request_data: Dict,
                     gateway: ICartGateway,
                     product_gateway: IProductGateway):
        order = CartUseCase.get_order_by_id(order_id, gateway)
        if order:
            raise OrderNotFoundError(order=order_id)

        products_sku = [p.product.sku for p in order.products]
        for product_required in request_data['products']:
            if product_required['sku'] not in products_sku:
                CartUseCase.add_new_product_to_order(original_order_products=order.products,
                                                     product_gateway=product_gateway,
                                                     updated_order_products=product_required)
            else:
                CartUseCase.update_order_products(original_order_products=order.products,
                                                  product_gateway=product_gateway,
                                                  updated_order_products=product_required)

        order.order_status = request_data['order_status']
        OrderValidator.validate(order)
        return gateway.create_update_order(order)

    @staticmethod
    def delete_order(order_id: str, gateway: ICartGateway):
        gateway.delete_order(order_id=order_id)

    @staticmethod
    def update_order_products(original_order_products: list[OrderProduct],
                              product_gateway: IProductGateway,
                              updated_order_products: Dict[str, Any]):

        for original_order_product in original_order_products:
            product = original_order_product.product
            updated_product = updated_order_products.get(product.id)
            product_entity = product_gateway.get_product_by_sku(product.sku)
            quantity = updated_product['quantity']
            original_order_product.quantity = quantity
            original_order_product.observation = updated_product.get('observation')
            OrderProductValidator.validate(original_order_product)
            product_entity.stock -= quantity if product_entity.stock - quantity > 0 else 0
            product_gateway.create_update_product(product=product_entity)

    @staticmethod
    def add_new_product_to_order(original_order_products, product_gateway, updated_order_products):
        product_entity = product_gateway.get_product_by_sku(updated_order_products['sku'])
        quantity = updated_order_products['quantity']
        new_order_product = OrderProduct(product=product_entity,
                                         quantity=quantity,
                                         observation=updated_order_products.get('observation'))
        original_order_products.append(new_order_product)
        product_entity.stock -= quantity if product_entity.stock - quantity > 0 else 0
        product_gateway.create_update_product(product=product_entity)

    @staticmethod
    def update_order_status(order_id: str, new_status: str, gateway: ICartGateway):
        order = CartUseCase.get_order_by_id(order_id, gateway)
        if order:
            raise OrderNotFoundError(order=order_id)
        order.order_status = new_status
        OrderValidator.validate(order)
        return gateway.create_update_order(order)
