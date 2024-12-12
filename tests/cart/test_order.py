import math
from datetime import datetime

import pytest

from src.cart.domain.domain_exception import OrderDomainException, OrderProductDomainException
from src.cart.domain.entities.order import Order
from src.cart.domain.entities.order_product import OrderProduct
from src.cart.domain.enums.order_status import OrderStatus
from src.cart.domain.enums.paymentConditions import PaymentConditions
from src.product.domain.entities.product import Product


def test_order_creation_valid():
    order = Order(
        user=1,
        order_datetime=datetime.now(),
        order_status=OrderStatus.PENDENTE,
        payment_condition=PaymentConditions.PIX)
    order.add_product(OrderProduct(product=Product(sku="12345678",
                                                   description="Darth Burger",
                                                   category="Lanche",
                                                   stock=100,
                                                   price=10.0),
                                   quantity=4))
    order.add_product(OrderProduct(product=Product(sku="09876542",
                                                   description="Burger Master",
                                                   category="Lanche",
                                                   stock=100,
                                                   price=30.0),
                                   quantity=2)
                      )
    assert order.id is not None
    assert math.isclose(order.total_order, 100.0, rel_tol=1e-09, abs_tol=1e-09)
    assert order.order_status == OrderStatus.PENDENTE
    assert order.payment_condition == PaymentConditions.PIX


def test_invalid_payment_condition():
    with pytest.raises(OrderDomainException) as exc_info:
        order = Order(
            user=1,
            order_datetime=datetime.now(),
            order_status=OrderStatus.PENDENTE,
            payment_condition="INVALID")  # noqa
        order.add_product(OrderProduct(product=Product(sku="12345678",
                                                       description="Darth Burger",
                                                       category="Lanche",
                                                       stock=100,
                                                       price=10.0),
                                       quantity=4))
        order.add_product(OrderProduct(product=Product(sku="09876542",
                                                       description="Burger Master",
                                                       category="Lanche",
                                                       stock=100,
                                                       price=30.0),
                                       quantity=2)
                          )
    assert str(exc_info.value) == "Forma de Pagamento inválida"


def test_invalid_order_status():
    with pytest.raises(OrderDomainException) as exc_info:
        order = Order(
            user=1,
            order_datetime=datetime.now(),
            order_status="INVALID",  # noqa
            payment_condition=PaymentConditions.PIX)

        order.add_product(OrderProduct(product=Product(sku="12345678",
                                                       description="Darth Burger",
                                                       category="Lanche",
                                                       stock=100,
                                                       price=10.0),
                                       quantity=4))
        order.add_product(OrderProduct(product=Product(sku="09876542",
                                                       description="Burger Master",
                                                       category="Lanche",
                                                       stock=100,
                                                       price=30.0),
                                       quantity=2)
                          )
    assert str(exc_info.value) == "Status do Pedido inválido"


def test_zero_product_quantity():
    with pytest.raises(OrderProductDomainException) as exc_info:
        OrderProduct(product=Product(sku="09876542",
                                     description="Burger Master",
                                     category="Lanche",
                                     stock=100,
                                     price=30.0),
                     quantity=0)
    assert str(exc_info.value) == "Quantidade do produto precisa ser maior que zero"


def test_negative_product_quantity():
    with pytest.raises(OrderProductDomainException) as exc_info:
        OrderProduct(product=Product(sku="09876542",
                                     description="Burger Master",
                                     category="Lanche",
                                     stock=100,
                                     price=30.0),
                     quantity=-1)
    assert str(exc_info.value) == "Quantidade do produto precisa ser maior que zero"
