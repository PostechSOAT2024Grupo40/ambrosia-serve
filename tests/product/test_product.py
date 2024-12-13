import pytest

from src.product.domain.entities.product import Product
from src.product.domain_exception import ProductDomainException


def test_valid_product():
    result = Product(name="Infused Rosemary & Onion Bear",
                     description="Darth Burger",
                     category="Lanche",
                     stock=100,
                     price=10.0)
    assert result
    assert result.description == "Darth Burger"
    assert result.category == "Lanche"
    assert result.stock == 100


def test_category_invalid():
    with pytest.raises(ProductDomainException) as exc:
        Product(name="Stir-Fried Pineapple Yak",
                description="Darth Burger",
                category="test",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Categoria de produto inválida"


def test_description_empty():
    with pytest.raises(ProductDomainException) as exc:
        Product(name="Roasted Thyme & Parsley Mammoth",
                description="",
                category="Lanche",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_description_null():
    with pytest.raises(ProductDomainException) as exc:
        Product(name="Dry-Roasted Fennel & Garlic Bear",
                description=None,  # noqa
                category="Lanche",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Descrição não pode ser vazio"


def test_price_less_or_equal_zero():
    with pytest.raises(ProductDomainException) as exc:
        Product(name="Baked Carrot & Coriander Lamb",
                description="Darth Burger",
                category="Lanche",
                stock=100,
                price=-10.0)
    assert str(exc.value) == "Preço não pode ser negativo ou igual a zero"


def test_stock_less_than_zero():
    with pytest.raises(ProductDomainException) as exc:
        Product(name="Simmered Blueberry & Mushroom Pork",
                description="Darth Burger",
                category="Lanche",
                stock=-100,
                price=10.0)
    assert str(exc.value) == "Estoque não pode ser negativo"


def test_name_empty():
    with pytest.raises(ProductDomainException) as exc:
        Product(name="",
                description="Darth Burger",
                category="Lanche",
                stock=100,
                price=10.0)
    assert str(exc.value) == "Nome não pode ser vazio"
