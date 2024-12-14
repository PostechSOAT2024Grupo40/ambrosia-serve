from unittest.mock import MagicMock

import pytest

from src.api.presentation.shared.enums.categories import Categories
from src.product.adapters.postgres_gateway import PostgreSqlProductGateway
from src.product.use_cases.create_product import CreateProductUseCase
from src.product.use_cases.delete_product import DeleteProductUseCase
from src.product.use_cases.get_all_products import GetAllProductsUseCase
from src.product.use_cases.get_product_by_id import GetProductByIdUseCase
from src.product.use_cases.update_product import UpdateProductUseCase
from tests.product.adapters.mock_product_gateway import MockProductGateway


@pytest.fixture
def mock_uow():
    uow = MagicMock()
    uow.repository.get_all = MagicMock()
    uow.repository.filter_by_id = MagicMock()
    uow.repository.insert_update = MagicMock()
    uow.repository.delete = MagicMock()
    uow.commit = MagicMock()
    return uow


@pytest.fixture
def gateway(mock_uow):
    return PostgreSqlProductGateway(mock_uow)

@pytest.fixture
def mock_gateway():
    return MockProductGateway()

@pytest.fixture
def update_product_usecase(mock_gateway):
    return UpdateProductUseCase(gateway=mock_gateway)


@pytest.fixture
def create_product_usecase(mock_gateway):
    return CreateProductUseCase(gateway=mock_gateway)


@pytest.fixture
def get_all_products_usecase(mock_gateway):
    return GetAllProductsUseCase(gateway=mock_gateway)


@pytest.fixture
def delete_product_usecase(mock_gateway):
    return DeleteProductUseCase(gateway=mock_gateway)


@pytest.fixture
def get_product_by_id_usecase(mock_gateway):
    return GetProductByIdUseCase(gateway=mock_gateway)


@pytest.fixture
def product_data():
    return {
        "name": "Test Product",
        "price": 100.0,
        "description": "A test product description",
        "stock": 50,
        "category": Categories.LANCHE,
    }
