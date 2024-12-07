from unittest.mock import MagicMock

import pytest

from src.product.adapters.postgres_gateway import PostgreSqlProductGateway


@pytest.fixture
def mock_uow():
    uow = MagicMock()
    uow.repository.get_all = MagicMock()
    uow.repository.filter_by_sku = MagicMock()
    uow.repository.insert_update = MagicMock()
    uow.repository.delete = MagicMock()
    uow.commit = MagicMock()
    return uow


@pytest.fixture
def gateway(mock_uow):
    return PostgreSqlProductGateway(mock_uow)
