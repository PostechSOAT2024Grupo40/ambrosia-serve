from src.cart.domain.domain_exception import OrderProductDomainException
from src.product.domain.entities.product import Product


class OrderProductValidator:
    @staticmethod
    def validate(order_product):
        if order_product.quantity <= 0:
            raise OrderProductDomainException("Quantidade do produto precisa ser maior que zero")

        if not isinstance(order_product.product, Product):
            raise OrderProductDomainException("Produto precisa ser do tipo `Product`")

        if order_product.product.price <= 0:
            raise OrderProductDomainException("Preço do produto precisa ser maior que zero")
