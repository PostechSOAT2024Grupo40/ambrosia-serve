from src.product.domain.object_values import generate_id
from src.product.domain.validators.product_validator import ProductValidator


class Product:
    def __init__(self,

                 name: str,
                 description: str,
                 category: str,
                 price: float,
                 stock: int,
                 image: str = "",
                 _id: str = None):
        self._id = _id or generate_id()
        self.name = name
        self.description = description
        self.category = category
        self.stock = stock
        self.price = price
        self.image = image

        ProductValidator.validate(product=self)

    @property
    def id(self):
        return self._id

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other: 'Product'):
        return self._id == other.id
