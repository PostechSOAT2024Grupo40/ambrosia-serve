from dataclasses import dataclass

from src.product.domain.entities.product import Product


@dataclass
class ProductDto:
    id: int
    sku: str
    description: str
    category: str
    price: float
    stock: int


def test_get_products(gateway, mock_uow):
    mock_uow.repository.get_all.return_value = [
        ProductDto(**{'id': 1, 'sku': 'sku1', 'description': 'desc1', 'category': 'Bebida', 'price': 100.0, 'stock': 10}),
        ProductDto(**{'id': 2, 'sku': 'sku2', 'description': 'desc2', 'category': 'Sobremesa', 'price': 200.0, 'stock': 20})
    ]

    products = gateway.get_products()

    assert len(products) == 2
    assert products[0].sku == 'sku1'
    assert products[1].price == 200.0
    mock_uow.repository.get_all.assert_called_once()


def test_get_product_by_sku(gateway, mock_uow):
    mock_uow.repository.filter_by_sku.return_value = ProductDto(**{
        'id': 1, 'sku': 'sku1', 'description': 'desc1', 'category': 'Bebida', 'price': 100.0, 'stock': 10
    })

    product = gateway.get_product_by_sku('sku1')

    assert product is not None
    assert product.sku == 'sku1'
    mock_uow.repository.filter_by_sku.assert_called_once_with('sku1')


def test_create_update_product(gateway, mock_uow):
    product = Product(_id=1, sku='sku1', description='desc1', category='Bebida', price=100.0, stock=10)

    updated_product = gateway.create_update_product(product)

    assert updated_product == product
    mock_uow.repository.insert_update.assert_called_once_with({
        'id': product.id, 'sku': product.sku, 'description': product.description,
        'category': product.category, 'price': product.price, 'stock': product.stock
    })
    mock_uow.commit.assert_called_once()


def test_delete_product(gateway, mock_uow):
    gateway.delete_product('sku1')

    mock_uow.repository.delete.assert_called_once_with('sku1')
    mock_uow.commit.assert_called_once()