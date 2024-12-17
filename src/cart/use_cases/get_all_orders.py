from src.cart.domain.entities.order import Order
from src.cart.domain.entities.order_product import OrderProduct
from src.cart.ports.cart_gateway import ICartGateway
from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway


class GetAllOrdersUseCase:
    def __init__(self, gateway: ICartGateway, product_gateway: IProductGateway):
        self.gateway = gateway
        self.product_gateway = product_gateway

    def execute(self):
        orders: list[Order] = self.gateway.get_orders()
        for order in orders:
            order_products: list[dict] = self.gateway.get_order_products(order_id=order.id)
            for row in order_products:
                product = self.product_gateway.get_product_by_id(row['product_id'])
                order.add_product(
                    product=OrderProduct(
                        product=Product(
                            _id=product.id,
                            name=product.name,
                            description=product.description,
                            category=product.category,
                            stock=product.stock,
                            price=product.price
                        ),
                        quantity=row['quantity'],
                        observation=row['observation']
                    )
                )

        return orders
