from src.product.domain.object_value.sku import generate_sku_from_description
from src.product.domain.validators.product_validator import ProductValidator


class Product:
    def __init__(self,
                 description: str,
                 category: str,
                 price: float,
                 stock: int):
        self.sku = generate_sku_from_description(description)
        self.description = description
        self.category = category
        self.stock = stock
        self.price = price

        ProductValidator.validate(product=self)

    def __hash__(self):
        return hash(self.sku)

    def __eq__(self, other):
        return self.sku == other.sku
