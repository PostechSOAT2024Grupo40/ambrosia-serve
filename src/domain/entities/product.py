import uuid

from src.domain.domain_exception import DomainException
from src.domain.enums.categories import Categories


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

        self.__validador()

    def __validador(self):
        try:
            Categories(self.category)
        except ValueError:
            raise DomainException("Categoria de produto inválida")
        if not self.description or not self.description.strip():
            raise DomainException("Descrição não pode ser vazio")
        if self.stock < 0:
            raise DomainException("Estoque não pode ser negativo")
        if self.price <= 0.0:
            raise DomainException("Preço não pode ser negativo ou igual a zero")
