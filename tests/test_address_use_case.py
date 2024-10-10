import pytest

from src.client.exceptions import AddressExistsError, AddressNotFoundError
from src.client.use_cases.address import AddressUseCase
from tests.mock_address_gateway import MockAddressGateway


@pytest.fixture
def mock_gateway():
    return MockAddressGateway()


@pytest.fixture
def sample_address_data():
    return {
        "id": 1,
        "street": "American street",
        "number": "3487"
    }


def test_create_new_address(mock_gateway, sample_address_data):
    address = AddressUseCase.create_new_address(sample_address_data, mock_gateway)

    assert address.street == sample_address_data["street"]
    assert address.number == sample_address_data["number"]


def test_create_existing_address(mock_gateway, sample_address_data):
    address_ = AddressUseCase.create_new_address(sample_address_data, mock_gateway)
    sample_address_data["id"] = address_.id

    with pytest.raises(AddressExistsError):
        AddressUseCase.create_new_address(sample_address_data, mock_gateway)


def test_update_address(mock_gateway, sample_address_data):
    address = AddressUseCase.create_new_address(sample_address_data, mock_gateway)

    updated_address = sample_address_data.copy()
    updated_address["number"] = "1234"
    updated_address["id"] = address.id

    updated_address_ = AddressUseCase.update_address(updated_address, mock_gateway)

    assert updated_address_.number == "1234"
    assert updated_address_.street == updated_address["street"]


def test_update_address_not_found(mock_gateway, sample_address_data):
    with pytest.raises(AddressNotFoundError):
        AddressUseCase.update_address(sample_address_data, mock_gateway)


def test_delete_address(mock_gateway, sample_address_data):
    address = AddressUseCase.create_new_address(sample_address_data, mock_gateway)
    AddressUseCase.delete_address(address.id, mock_gateway)
    with pytest.raises(AddressNotFoundError):
        AddressUseCase.delete_address(address.id, mock_gateway)


def test_get_address_by_cpf(mock_gateway, sample_address_data):
    address = AddressUseCase.create_new_address(sample_address_data, mock_gateway)

    found = AddressUseCase.get_by_id(address.id, mock_gateway)

    assert found.id == address.id


def test_get_address_by_cpf_not_found(mock_gateway, sample_address_data):
    address = AddressUseCase.get_by_id(99999, mock_gateway)

    assert address is None


def test_get_addresses(mock_gateway, sample_address_data):
    AddressUseCase.create_new_address(sample_address_data, mock_gateway)
    second_address_data = sample_address_data.copy()
    second_address_data["number"] = "234"
    second_address_data["streey"] = "one street"
    AddressUseCase.create_new_address(second_address_data, mock_gateway)

    addresses = AddressUseCase.get_addresses(mock_gateway)

    assert len(addresses) == 2
