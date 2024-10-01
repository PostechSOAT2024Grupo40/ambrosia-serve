import uuid

from src.domain_exception import DomainException
from src.enums.categorias import Categorias


class Produto:
    def __init__(self,
                 descricao: str,
                 categoria: str,
                 preco: float,
                 estoque: int):
        self.id = str(uuid.uuid4())
        self.descricao = descricao
        self.categoria = categoria
        self.estoque = estoque
        self.preco = preco

        self.__validador()

    def __validador(self):
        try:
            Categorias(self.categoria)
        except ValueError:
            raise DomainException("Categoria de produto inválida")
        if not self.descricao or not self.descricao.strip():
            raise DomainException("Descrição não pode ser vazio")
        if self.estoque < 0:
            raise DomainException("Estoque não pode ser negativo")
        if self.preco <= 0.0:
            raise DomainException("Preço não pode ser negativo ou igual a zero")
