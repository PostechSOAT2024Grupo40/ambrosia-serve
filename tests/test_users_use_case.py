import pytest

from src.client.exceptions import UserExistsError, UserNotFoundError
from src.client.use_cases.user import UsersUseCase
from tests.mock_user_gateway import MockUserGateway


@pytest.fixture
def mock_gateway():
    return MockUserGateway()


@pytest.fixture
def sample_user_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "cpf": "12345678901",
        "email": "john.doe@example.com",
        "password": "securePassword1"
    }


def test_create_new_user_success(mock_gateway, sample_user_data):
    user = UsersUseCase.create_new_user(sample_user_data, mock_gateway)

    assert user.cpf == sample_user_data["cpf"]
    assert user.email == sample_user_data["email"]
    assert user.password == sample_user_data["password"]


def test_create_new_user_already_exists(mock_gateway, sample_user_data):
    UsersUseCase.create_new_user(sample_user_data, mock_gateway)

    with pytest.raises(UserExistsError):
        UsersUseCase.create_new_user(sample_user_data, mock_gateway)


def test_update_user_success(mock_gateway, sample_user_data):
    user = UsersUseCase.create_new_user(sample_user_data, mock_gateway)
    updated_data = sample_user_data.copy()
    updated_data["first_name"] = "Jane"

    updated_user = UsersUseCase.update_user(updated_data, mock_gateway)

    assert updated_user.first_name == "Jane"
    assert updated_user.cpf == sample_user_data["cpf"]


def test_update_user_not_found(mock_gateway, sample_user_data):
    with pytest.raises(UserNotFoundError):
        UsersUseCase.update_user(sample_user_data, mock_gateway)


def test_delete_user_success(mock_gateway, sample_user_data):
    user = UsersUseCase.create_new_user(sample_user_data, mock_gateway)

    UsersUseCase.delete_user(user.cpf, mock_gateway)

    with pytest.raises(UserNotFoundError):
        UsersUseCase.delete_user(user.cpf, mock_gateway)


def test_get_user_by_cpf(mock_gateway, sample_user_data):
    UsersUseCase.create_new_user(sample_user_data, mock_gateway)

    user = UsersUseCase.get_user_by_cpf(sample_user_data["cpf"], mock_gateway)

    assert user.cpf == sample_user_data["cpf"]


def test_get_user_by_cpf_not_found(mock_gateway, sample_user_data):
    user = UsersUseCase.get_user_by_cpf("nonexistentcpf", mock_gateway)

    assert user is None


def test_get_users(mock_gateway, sample_user_data):
    UsersUseCase.create_new_user(sample_user_data, mock_gateway)
    second_user_data = sample_user_data.copy()
    second_user_data["cpf"] = "98765432100"
    second_user_data["email"] = "jane.doe@example.com"
    UsersUseCase.create_new_user(second_user_data, mock_gateway)

    users = UsersUseCase.get_users(mock_gateway)

    assert len(users) == 2
