import pytest

from src.product.domain.entities.product import Product
from src.product.domain_exception import ProductDomainException


def test_valid_product():
    result = Product(description="Darth Burger",
                     category="Lanche",
                     stock=100,
                     price=10.0)
    assert result is not None
    assert result.description == "Darth Burger"
    assert result.category == "Lanche"
    assert result.stock == 100


def test_category_invalid():
    with pytest.raises(ProductDomainException) as exc:
        Product(description="Darth Burger",
                category="test",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Categoria de produto inválida"


def test_description_empty():
    with pytest.raises(ProductDomainException) as exc:
        Product(description="",
                category="Lanche",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_description_null():
    with pytest.raises(ProductDomainException) as exc:
        Product(description=None,  # noqa
                category="Lanche",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_price_less_or_equal_zero():
    with pytest.raises(ProductDomainException) as exc:
        Product(description="Darth Burger",
                category="Lanche",
                stock=100,
                price=-10.0)
    assert str(exc.value) == "Preço não pode ser negativo ou igual a zero"


def test_stock_less_than_zero():
    with pytest.raises(ProductDomainException) as exc:
        Product(description="Darth Burger",
                category="Lanche",
                stock=-100,
                price=10.0)
    assert str(exc.value) == "Estoque não pode ser negativo"
