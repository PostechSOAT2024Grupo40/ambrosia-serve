from src.cart.domain.entities.order import Order


class OrderPlacedEvent:
    def __init__(self, product_id: str, quantity: int, order_id: str):
        self.product_id = product_id
        self.quantity = quantity
        self.order_id = order_id

    def publish(self, order_created: Order):
        pass
