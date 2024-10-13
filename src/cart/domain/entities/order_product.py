from src.cart.domain.object_values import generate_id
from src.cart.domain.validators.order_product_validator import OrderProductValidator
from src.product.domain.entities.product import Product


class OrderProduct:
    def __init__(self, product: Product, quantity: int, _id: str = generate_id()):
        self._id = _id
        self.product = product
        self.quantity = quantity

        OrderProductValidator.validate(order_product=self)

    @property
    def id(self):
        return self._id

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return self._id == other.id
