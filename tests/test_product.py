import pytest

from src.domain.domain_exception import DomainException
from src.domain.entities.product import Product


def test_produto_valido():
    resultado = Product(description="Darth Burger",
                        category="Lanche",
                        stock=100,
                        price=10.0)
    assert resultado is not None
    assert resultado.description == "Darth Burger"
    assert resultado.category == "Lanche"
    assert resultado.stock == 100


def test_categoria_invalida():
    with pytest.raises(DomainException) as exc:
        Product(description="Darth Burger",
                category="test",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Categoria de produto inválida"


def test_descricao_vazia():
    with pytest.raises(DomainException) as exc:
        Product(description="",
                category="Lanche",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_descricao_nula():
    with pytest.raises(DomainException) as exc:
        Product(description=None,  # noqa
                category="Lanche",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_preco_menor_ou_igual_a_zero():
    with pytest.raises(DomainException) as exc:
        Product(description="Darth Burger",
                category="Lanche",
                stock=100,
                price=-10.0)
    assert str(exc.value) == "Preço não pode ser negativo ou igual a zero"


def test_estoque_menor_que_zero():
    with pytest.raises(DomainException) as exc:
        Product(description="Darth Burger",
                category="Lanche",
                stock=-100,
                price=10.0)
    assert str(exc.value) == "Estoque não pode ser negativo"
