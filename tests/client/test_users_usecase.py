import pytest

from src.client.domain.entities.user import User
from src.client.exceptions import UserExistsError, UserNotFoundError
from tests.client.mock_user_gateway import MockUserGateway


def test_create_new_user_success(mock_gateway, sample_user_data, create_user_usecase):
    user = create_user_usecase.execute(sample_user_data)

    assert user.cpf == sample_user_data["cpf"]
    assert user.email == sample_user_data["email"]
    assert user.password == sample_user_data["password"]


def test_create_new_user_already_exists(mock_gateway, sample_user_data, create_user_usecase):
    create_user_usecase.execute(sample_user_data)

    with pytest.raises(UserExistsError):
        create_user_usecase.execute(sample_user_data)


def test_update_user_success(mock_gateway, sample_user_data, create_user_usecase, update_user_usecase):
    create_user_usecase.execute(sample_user_data)
    updated_data = sample_user_data.copy()
    updated_data["first_name"] = "Jane"

    updated_user = update_user_usecase.execute(updated_data)

    assert updated_user.first_name == "Jane"
    assert updated_user.cpf == sample_user_data["cpf"]


def test_update_user_not_found(mock_gateway, sample_user_data, update_user_usecase):
    with pytest.raises(UserNotFoundError):
        update_user_usecase.execute(sample_user_data)


def test_delete_user_success(mock_gateway, sample_user_data, create_user_usecase, delete_user_usecase):
    user = create_user_usecase.execute(sample_user_data)

    delete_user_usecase.execute(user.id)

    with pytest.raises(UserNotFoundError):
        delete_user_usecase.execute(user.id)


def test_get_user_by_cpf(mock_gateway, sample_user_data, create_user_usecase, get_user_by_cpf_usecase):
    create_user_usecase.execute(sample_user_data)

    user = get_user_by_cpf_usecase.execute(sample_user_data["cpf"])

    assert user.cpf == sample_user_data["cpf"]


def test_get_user_by_cpf_not_found(mock_gateway, sample_user_data, get_user_by_cpf_usecase):

    with pytest.raises(UserNotFoundError):
        get_user_by_cpf_usecase.execute("nonexistentcpf")


def test_get_users(sample_user_data):
    gateway = MockUserGateway()

    user1 = User(_id="1", **sample_user_data)
    user2 = User(_id="2",
                 first_name="Jane",
                 last_name="Doe",
                 cpf="23456789012",
                 email="jane@mail.com",
                 password="123456123123")

    gateway.create_user(user1)
    gateway.create_user(user2)

    users = gateway.get_users()

    assert len(users) == 2
