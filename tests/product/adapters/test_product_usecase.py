import math

import pytest

from src.product.domain.entities.product import Product
from src.product.exceptions import ProductExistsError
from tests.product.adapters.mock_product_gateway import MockProductGateway


def test_create_product(create_product_usecase, product_data):
    product = create_product_usecase.execute(product_data)

    assert product.name == product_data["name"]


def test_update_product(update_product_usecase, create_product_usecase, product_data):
    _product = create_product_usecase.execute(product_data)
    updated_data = product_data.copy()
    updated_data["price"] = 120.0

    updated_product = update_product_usecase.execute(product_id=_product.id, request_data=updated_data)

    assert math.isclose(updated_product.price, 120.0, rel_tol=1e-09, abs_tol=1e-09)
    assert updated_product.id == _product.id


def test_get_product_by_id(get_product_by_id_usecase, create_product_usecase, product_data):
    _product = create_product_usecase.execute(product_data)

    product = get_product_by_id_usecase.execute(_product.id)

    assert product.id == _product.id
    assert product.name == product_data["name"]


def test_delete_product(delete_product_usecase, create_product_usecase, get_product_by_id_usecase, product_data):
    _product = create_product_usecase.execute(product_data)

    delete_product_usecase.execute(_product.id)

    product = get_product_by_id_usecase.execute(_product.id)

    assert product is None


def test_get_product_by_id_not_found(get_product_by_id_usecase):
    product = get_product_by_id_usecase.execute("nonexistentid")

    assert product is None


def test_create_product_usecase_product_exists(create_product_usecase, product_data):
    create_product_usecase.execute(product_data)

    with pytest.raises(ProductExistsError):
        create_product_usecase.execute(product_data)


def test_get_products():
    gateway = MockProductGateway()

    product1 = Product(_id="1", name="Product 1", description="Description 1", price=10.0, category="Lanche", stock=10)
    product2 = Product(_id="2", name="Product 2", description="Description 2", price=20.0, category="Lanche", stock=10)

    gateway.create_update_product(product1)
    gateway.create_update_product(product2)

    products = gateway.get_products()

    assert len(products) == 2
    assert product1 in products
    assert product2 in products
