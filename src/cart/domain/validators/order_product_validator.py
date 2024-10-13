from src.cart.domain.domain_exception import OrderProductDomainException
from src.product.domain.entities.product import Product

TEXT_MAX_SIZE = 100


class OrderProductValidator:
    @staticmethod
    def validate(order_product):
        if order_product.quantity <= 0:
            raise OrderProductDomainException("Quantidade do produto precisa ser maior que zero")

        if not isinstance(order_product.product, Product):
            raise OrderProductDomainException("Produto precisa ser do tipo `Product`")

        if order_product.product.price <= 0:
            raise OrderProductDomainException("Preço do produto precisa ser maior que zero")

        if order_product.product.stock < order_product.quantity:
            raise OrderProductDomainException("Produto sem estoque")

        if order_product.observation.strip() and len(order_product.observation) > TEXT_MAX_SIZE:
            raise OrderProductDomainException("Campo observação tem um tamanho máximo de 100 caracteres")
