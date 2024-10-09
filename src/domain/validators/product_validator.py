from src.domain.domain_exception import DomainException
from src.domain.enums.categories import Categories


class ProductValidator:

    @staticmethod
    def validate(product):
        try:
            Categories(product.category)
        except ValueError:
            raise DomainException("Categoria de produto inválida")

        if not product.description or not product.description.strip():
            raise DomainException("Descrição não pode ser vazio")

        if product.stock < 0:
            raise DomainException("Estoque não pode ser negativo")

        if product.price <= 0.0:
            raise DomainException("Preço não pode ser negativo ou igual a zero")
