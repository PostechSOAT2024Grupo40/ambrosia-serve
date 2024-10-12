from src.product.domain.validators.product_validator import ProductValidator
from src.product.domain.object_values import generate_id


class Product:
    def __init__(self,
                 sku: str,
                 description: str,
                 category: str,
                 price: float,
                 stock: int,
                 _id: int = generate_id()):
        self._id = _id
        self.sku = sku
        self.description = description
        self.category = category
        self.stock = stock
        self.price = price

        ProductValidator.validate(product=self)

    def __hash__(self):
        return hash(self.sku)

    def __eq__(self, other):
        return self.sku == other.sku
    @property
    def id(self):
        return self._id
