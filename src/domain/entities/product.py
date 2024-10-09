import uuid

from src.domain.validators.product_validator import ProductValidator


class Product:
    def __init__(self,
                 description: str,
                 category: str,
                 price: float,
                 stock: int):
        self.id = str(uuid.uuid4())
        self.description = description
        self.category = category
        self.stock = stock
        self.price = price

        ProductValidator.validate(product=self)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
