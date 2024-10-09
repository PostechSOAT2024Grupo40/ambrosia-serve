from src.cart.domain.domain_exception import OrderDomainException
from src.cart.domain.enums.categories import Categories


class ProductValidator:

    @staticmethod
    def validate(product):
        try:
            Categories(product.category)
        except ValueError:
            raise OrderDomainException("Categoria de produto inválida")

        if not product.description or not product.description.strip():
            raise OrderDomainException("Descrição não pode ser vazio")

        if product.stock < 0:
            raise OrderDomainException("Estoque não pode ser negativo")

        if product.price <= 0.0:
            raise OrderDomainException("Preço não pode ser negativo ou igual a zero")
