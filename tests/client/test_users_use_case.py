import pytest

from src.client.exceptions import UserExistsError, UserNotFoundError


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
    user = get_user_by_cpf_usecase.execute("nonexistentcpf")

    assert user is None


def test_get_users(mock_gateway, sample_user_data, create_user_usecase, get_all_users_usecase):
    create_user_usecase.execute(sample_user_data)
    second_user_data = sample_user_data.copy()
    second_user_data["cpf"] = "98765432100"
    second_user_data["email"] = "jane.doe@example.com"
    create_user_usecase.execute(second_user_data)

    users = get_all_users_usecase.execute()

    assert len(users) == 2
