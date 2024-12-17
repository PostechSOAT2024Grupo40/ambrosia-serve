import pytest

from src.cart.exceptions import ClientError, ProductNotFoundError
from src.cart.use_cases.create_cart import CreateCartUseCase


def test_create_new_order_user_not_found(request_data, mock_cart_gateway, mock_user_gateway, mock_product_gateway):
    mock_user_gateway.get_user_by_id.return_value = None
    use_case = CreateCartUseCase(cart_gateway=mock_cart_gateway, user_gateway=mock_user_gateway,
                                 product_gateway=mock_product_gateway,
                                 get_order_by_id=mock_cart_gateway.get_order_by_id)

    with pytest.raises(ClientError):
        use_case.execute(
            request_data=request_data)


def test_create_new_order_product_not_found(request_data, mock_cart_gateway, mock_user_gateway, mock_product_gateway):
    mock_user_gateway.get_user_by_id.return_value = {"id": "user123", "name": "Test User"}
    mock_product_gateway.get_product_by_id.side_effect = [None]
    use_case = CreateCartUseCase(cart_gateway=mock_cart_gateway, user_gateway=mock_user_gateway,
                                 product_gateway=mock_product_gateway,
                                 get_order_by_id=mock_cart_gateway.get_order_by_id)

    with pytest.raises(ProductNotFoundError):
        use_case.execute(
            request_data=request_data)
