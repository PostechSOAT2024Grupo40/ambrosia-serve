from src.product.domain_exception import ProductDomainException
from src.shared.enums.categories import Categories


class ProductValidator:

    @staticmethod
    def validate(product):
        try:
            Categories(product.category)
        except ValueError:
            raise ProductDomainException("Categoria de produto inválida")

        if not product.description or not product.description.strip():
            raise ProductDomainException("Descrição não pode ser vazio")

        if product.stock < 0:
            raise ProductDomainException("Estoque não pode ser negativo")

        if product.price <= 0.0:
            raise ProductDomainException("Preço não pode ser negativo ou igual a zero")

        if not product.sku:
            raise ProductDomainException("Sku inválida")
