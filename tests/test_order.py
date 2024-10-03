from datetime import datetime

import pytest

from src.domain.domain_exception import DomainException
from src.domain.entities.order import Order
from src.domain.enums.order_status import OrderStatus
from src.domain.enums.paymentConditions import PaymentConditions


def test_order_creation_valid():
    order = Order(
        user=1,
        user_address=1,
        total_order=100.0,
        delivery_value=10.0,
        product_quantity=2,
        order_datetime=datetime.now(),
        order_status=OrderStatus.PENDENTE,
        payment_condition=PaymentConditions.PIX
    )
    assert order.id is not None
    assert order.total_order == 100.0
    assert order.delivery_value == 10.0
    assert order.product_quantity == 2
    assert order.order_status == OrderStatus.PENDENTE
    assert order.payment_condition == PaymentConditions.PIX


def test_invalid_payment_condition():
    with pytest.raises(DomainException) as exc_info:
        Order(
            user=1,
            user_address=1,
            total_order=100.0,
            delivery_value=10.0,
            product_quantity=2,
            order_datetime=datetime.now(),
            order_status=OrderStatus.PENDENTE,
            payment_condition="INVALID"  # noqa
        )
    assert str(exc_info.value) == "Forma de Pagamento inválida"


def test_invalid_order_status():
    with pytest.raises(DomainException) as exc_info:
        Order(
            user=1,
            user_address=1,
            total_order=100.0,
            delivery_value=10.0,
            product_quantity=2,
            order_datetime=datetime.now(),
            order_status="INVALID",  # noqa
            payment_condition=PaymentConditions.PIX
        )
    assert str(exc_info.value) == "Status do Pedido inválido"


def test_negative_total_order():
    with pytest.raises(DomainException) as exc_info:
        Order(
            user=1,
            user_address=1,
            total_order=-50.0,
            delivery_value=10.0,
            product_quantity=2,
            order_datetime=datetime.now(),
            order_status=OrderStatus.PENDENTE,
            payment_condition=PaymentConditions.PIX
        )
    assert str(exc_info.value) == "O valor total não pode ser menor ou igual a zero"


def test_zero_total_order():
    with pytest.raises(DomainException) as exc_info:
        Order(
            user=1,
            user_address=1,
            total_order=0.0,
            delivery_value=10.0,
            product_quantity=2,
            order_datetime=datetime.now(),
            order_status=OrderStatus.PENDENTE,
            payment_condition=PaymentConditions.PIX
        )
    assert str(exc_info.value) == "O valor total não pode ser menor ou igual a zero"


def test_negative_delivery_value():
    with pytest.raises(DomainException) as exc_info:
        Order(
            user=1,
            user_address=1,
            total_order=100.0,
            delivery_value=-5.0,
            product_quantity=2,
            order_datetime=datetime.now(),
            order_status=OrderStatus.PENDENTE,
            payment_condition=PaymentConditions.PIX
        )
    assert str(exc_info.value) == "O valor de entrega não pode ser negativo"


def test_zero_product_quantity():
    with pytest.raises(DomainException) as exc_info:
        Order(
            user=1,
            user_address=1,
            total_order=100.0,
            delivery_value=10.0,
            product_quantity=0,
            order_datetime=datetime.now(),
            order_status=OrderStatus.PENDENTE,
            payment_condition=PaymentConditions.PIX
        )
    assert str(exc_info.value) == "A quantidade de produtos não pode ser menor ou igual a zero"


def test_negative_product_quantity():
    with pytest.raises(DomainException) as exc_info:
        Order(
            user=1,
            user_address=1,
            total_order=100.0,
            delivery_value=10.0,
            product_quantity=-1,
            order_datetime=datetime.now(),
            order_status=OrderStatus.PENDENTE,
            payment_condition=PaymentConditions.PIX
        )
    assert str(exc_info.value) == "A quantidade de produtos não pode ser menor ou igual a zero"
