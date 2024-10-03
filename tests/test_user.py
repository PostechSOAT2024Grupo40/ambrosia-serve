import pytest

from src.domain.domain_exception import DomainException
from src.domain.entities.user import User


def test_usuario_valido():
    resultado = User(first_name="Joaão",
                     last_name="da Silva",
                     cpf="66007637018",
                     email="j.silva@hotmail.com",
                     password="12345678",
                     address=["rua 1"])
    assert resultado is not None
    assert resultado.cpf == "66007637018"
    assert resultado.email == "j.silva@hotmail.com"
    assert resultado.password == "12345678"
    assert resultado.address == ["rua 1"]


def test_cpf_nao_formato_deve_retornar_erro():
    with pytest.raises(DomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="660.076.370-19",
             email="j.silva@hotmail.com",
             password="12345678",
             address=["rua 1"])

    assert str(exc.value) == "CPF inválido"


def test_cpf_vazio_deve_retornar_erro():
    with pytest.raises(DomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf=None,  # noqa
             email="j.silva@gmail.com",
             password="12345678",
             address=["rua 1"])

    assert str(exc.value) == "CPF não pode ser vazio"


def test_email_invalido_deve_retornar_erro():
    with pytest.raises(DomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva",
             password="12345678",
             address=["rua 1"])

    assert str(exc.value) == "Email inválido"


def test_email_vazio_deve_retornar_erro():
    with pytest.raises(DomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email=None,  # noqa
             password="12345678",
             address=["rua 1"])

    assert str(exc.value) == "Email não pode ser vazio"


def test_senha_menor_que_8_caracteres_deve_retornar_erro():
    with pytest.raises(DomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password="1234567",
             address=["rua 1"])

    assert str(exc.value) == "Senha deve ter pelo menos 8 caracteres"


def test_senha_vazio_deve_retornar_erro():
    with pytest.raises(DomainException) as exc:
        User(first_name="Joaão",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password=None,  # noqa
             address=["rua 1"])

    assert str(exc.value) == "Senha não pode ser vazia"


def test_nome_invalidos():
    with pytest.raises(DomainException) as exc_nome:
        User(first_name="",
             last_name="da Silva",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password="12345678",
             address=["rua 1"])

    assert str(exc_nome.value) == "Nome não pode ser vazio"


def test_sobrenome_invalidos():
    with pytest.raises(DomainException) as exc_sobrenome:
        User(first_name="Joaão",
             last_name="",
             cpf="66007637018",
             email="j.silva@gmail.com",
             password="12345678",
             address=["rua 1"])

    assert str(exc_sobrenome.value) == "Sobrenome não pode ser vazio"
