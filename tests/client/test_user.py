import pytest

from src.client.domain.domain_exception import ClientDomainException
from src.client.domain.entities.user import User


def test_user_valid():
    result = User(first_name="Joaão",
                  last_name="da Silva",
                  cpf="66007637018",
                  email="j.silva@hotmail.com",
                  password="12345678")
    assert result is not None
    assert result.cpf == "66007637018"
    assert result.email == "j.silva@hotmail.com"
    assert result.password == "12345678"


def test_cpf_in_wrong_format_should_return_error():
    with pytest.raises(ClientDomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="660.076.370-19",
             email="j.silva@hotmail.com",
             password="12345678")

    assert str(exc.value) == "CPF inválido"


def test_cpf_empty_should_return_error():
    with pytest.raises(ClientDomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf=None,  # noqa
             email="j.silva@gmail.com",
             password="12345678")

    assert str(exc.value) == "CPF não pode ser vazio"


def test_invalid_email_should_return_error():
    with pytest.raises(ClientDomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva",
             password="12345678")

    assert str(exc.value) == "Email inválido"


def test_empty_email_should_return_error():
    with pytest.raises(ClientDomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email=None,  # noqa
             password="12345678")

    assert str(exc.value) == "Email não pode ser vazio"


def test_password_less_than_8_caracteres_should_return_error():
    with pytest.raises(ClientDomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password="1234567")

    assert str(exc.value) == "Senha deve ter pelo menos 8 caracteres"


def test_empty_password_should_return_error():
    with pytest.raises(ClientDomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password=None  # noqa
             )

    assert str(exc.value) == "Senha não pode ser vazia"


def test_invalid_first_name():
    with pytest.raises(ClientDomainException) as exc_nome:
        User(first_name="",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password="12345678")

    assert str(exc_nome.value) == "Nome não pode ser vazio"


def test_invalid_last_name():
    with pytest.raises(ClientDomainException) as exc_sobrenome:
        User(first_name="Joaão",
             last_name="",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password="12345678")

    assert str(exc_sobrenome.value) == "Sobrenome não pode ser vazio"


def test_objects_are_equal():
    user_1 = User(first_name="Joaão",
                  last_name="da Silva",
                  cpf="66007637018",
                  email="j.silva@gmail.com",
                  password="12345678")

    user_2 = User(first_name="Joaão",
                  last_name="da Silva",
                  cpf="66007637018",
                  email="j.silva@gmail.com",
                  password="12345678")
    assert user_1 == user_2


def test_hashes_are_equal():
    user_1 = User(first_name="Joaão",
                  last_name="da Silva",
                  cpf="66007637018",
                  email="j.silva@gmail.com",
                  password="12345678")

    user_2 = User(first_name="Joaão",
                  last_name="da Silva",
                  cpf="66007637018",
                  email="j.silva@gmail.com",
                  password="12345678")
    assert user_1 == user_2
