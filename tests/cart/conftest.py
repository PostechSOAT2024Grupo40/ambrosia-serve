from unittest.mock import Mock

import pytest


@pytest.fixture
def mock_cart_gateway():
    return Mock()


@pytest.fixture
def mock_user_gateway():
    return Mock()


@pytest.fixture
def mock_product_gateway():
    return Mock()


@pytest.fixture
def request_data():
    return {
        "user_id": "user123",
        "products": [
            {"product_id": "prod1", "quantity": 2},
            {"product_id": "prod2", "quantity": 1},
        ],
        "payment_condition": "Dinheiro",
    }
