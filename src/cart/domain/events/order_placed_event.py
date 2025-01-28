from src.cart.domain.entities.order import Order


class OrderPlacedEvent:

    def publish(self, data: list[tuple[str, int]]):
        pass
