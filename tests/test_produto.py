import pytest

from src.domain_exception import DomainException
from src.produto import Produto


def test_produto_valido():
    resultado = Produto(descricao="Darth Burger",
                        categoria="Lanche",
                        estoque=100,
                        preco=10.0)
    assert resultado is not None
    assert resultado.descricao == "Darth Burger"
    assert resultado.categoria == "Lanche"
    assert resultado.estoque == 100


def test_categoria_invalida():
    with pytest.raises(DomainException) as exc:
        Produto(descricao="Darth Burger",
                categoria="test",
                estoque=100,
                preco=10.0)
    assert str(exc.value) == "Categoria de produto inválida"


def test_descricao_vazia():
    with pytest.raises(DomainException) as exc:
        Produto(descricao="",
                categoria="Lanche",
                estoque=100,
                preco=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_descricao_nula():
    with pytest.raises(DomainException) as exc:
        Produto(descricao=None,  # noqa
                categoria="Lanche",
                estoque=100,
                preco=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_preco_menor_ou_igual_a_zero():
    with pytest.raises(DomainException) as exc:
        Produto(descricao="Darth Burger",
                categoria="Lanche",
                estoque=100,
                preco=-10.0)
    assert str(exc.value) == "Preço não pode ser negativo ou igual a zero"


def test_estoque_menor_que_zero():
    with pytest.raises(DomainException) as exc:
        Produto(descricao="Darth Burger",
                categoria="Lanche",
                estoque=-100,
                preco=10.0)
    assert str(exc.value) == "Estoque não pode ser negativo"
