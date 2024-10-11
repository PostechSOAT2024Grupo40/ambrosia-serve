from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway

from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class InMemoryProductGateway(IProductGateway):
    def __init__(self, uow: IProductUnitOfWork):
        self.uow = uow

    def get_products(self):
        products = self.uow.repository.get_all()
        if not products:
            return []
        return [Product(description=p['description'],
                        category=p['category'],
                        price=p['price'],
                        stock=p['stock']) for p in products]

    def get_product_by_sku(self, sku: str):
        result = self.uow.repository.filter_by_sku(sku)
        if not result:
            return
        product = Product(description=result['description'],
                          category=result['category'],
                          price=result['price'],
                          stock=result['stock'])
        return product

    def create_update_product(self, product: Product):
        self.uow.repository.insert_update({'sku': product.sku,
                                           'category': product.category,
                                           'description': product.description,
                                           'stock': product.stock,
                                           'price': product.price})
        self.uow.commit()
        return product

    def delete_product(self, sku: str):
        self.uow.repository.delete(sku)
        self.uow.commit()
