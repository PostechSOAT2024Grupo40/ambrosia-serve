import pytest

from src.cart.exceptions import ClientError, ProductNotFoundError
from src.cart.use_cases.cart import CartUseCase
from src.product.domain.entities.product import Product


def test_create_new_order_successfully(request_data, mock_cart_gateway, mock_user_gateway, mock_product_gateway):
    mock_user_gateway.get_user_by_id.return_value = {"id": "user123", "name": "Test User"}
    mock_product_gateway.get_product_by_id.side_effect = [
        Product(stock=5, _id="prod1", price=10.0, name="Product 1", description="Description 1", category="Lanche"),
        Product(stock=3, _id="prod2", price=15.0, name="Product 2", description="Description 2", category="Lanche"),
    ]
    mock_cart_gateway.get_order_by_id.return_value = None

    result = CartUseCase.create_new_order(
        request_data=request_data,
        cart_gateway=mock_cart_gateway,
        user_gateway=mock_user_gateway,
        product_gateway=mock_product_gateway,
    )

    assert result is not None
    mock_cart_gateway.create_update_order.assert_called_once()


def test_create_new_order_user_not_found(request_data, mock_cart_gateway, mock_user_gateway, mock_product_gateway):
    mock_user_gateway.get_user_by_id.return_value = None

    with pytest.raises(ClientError):
        CartUseCase.create_new_order(
            request_data=request_data,
            cart_gateway=mock_cart_gateway,
            user_gateway=mock_user_gateway,
            product_gateway=mock_product_gateway,
        )


def test_create_new_order_product_not_found(request_data, mock_cart_gateway, mock_user_gateway, mock_product_gateway):
    mock_user_gateway.get_user_by_id.return_value = {"id": "user123", "name": "Test User"}
    mock_product_gateway.get_product_by_id.side_effect = [None]

    with pytest.raises(ProductNotFoundError):
        CartUseCase.create_new_order(
            request_data=request_data,
            cart_gateway=mock_cart_gateway,
            user_gateway=mock_user_gateway,
            product_gateway=mock_product_gateway,
        )
