import pytest

from src.client.use_cases.create_use import CreateUserUseCase
from src.client.use_cases.delete_user import DeleteUserUseCase
from src.client.use_cases.get_all_users import GetAllUsersUseCase
from src.client.use_cases.get_user_by_cpf import GetUserByCpfUseCase
from src.client.use_cases.update_user import UpdateUserUseCase
from tests.client.mock_user_gateway import MockUserGateway


@pytest.fixture
def mock_gateway():
    return MockUserGateway()


@pytest.fixture
def create_user_usecase(mock_gateway):
    return CreateUserUseCase(gateway=mock_gateway)


@pytest.fixture
def update_user_usecase(mock_gateway):
    return UpdateUserUseCase(gateway=mock_gateway)


@pytest.fixture
def delete_user_usecase(mock_gateway):
    return DeleteUserUseCase(gateway=mock_gateway)


@pytest.fixture
def get_user_by_cpf_usecase(mock_gateway):
    return GetUserByCpfUseCase(gateway=mock_gateway)


@pytest.fixture
def get_all_users_usecase(mock_gateway):
    return GetAllUsersUseCase(gateway=mock_gateway)


@pytest.fixture
def sample_user_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "cpf": "12345678901",
        "email": "john.doe@example.com",
        "password": "securePassword1"
    }
