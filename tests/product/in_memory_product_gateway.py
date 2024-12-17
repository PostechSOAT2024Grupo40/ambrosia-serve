from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway

from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class InMemoryProductGateway(IProductGateway):

    def __init__(self, uow: IProductUnitOfWork):
        self.uow = uow

    def get_product_by_name(self, product_name: str):
        product = self.uow.repository.find_by_name(product_name)
        if not product:
            return
        return Product(_id=product['id'],
                       name=product['name'],
                       description=product['description'],
                       category=product['category'],
                       price=product['price'],
                       stock=product['stock'])

    def get_products(self):
        products = self.uow.repository.get_all()
        if not products:
            return []
        return [
            Product(_id=p['id'],
                    name=p['name'],
                    description=p['description'],
                    category=p['category'],
                    price=p['price'],
                    stock=p['stock'])
            for p in products]

    def get_product_by_id(self, product_id: str):
        result = self.uow.repository.filter_by_id(product_id)
        if not result:
            return
        product = Product(_id=result['id'],
                          name=result['name'],
                          description=result['description'],
                          category=result['category'],
                          price=result['price'],
                          stock=result['stock'])
        return product

    def create_update_product(self, product: Product):
        self.uow.repository.insert_update({'is': product.id,
                                           'name': product.name,
                                           'category': product.category,
                                           'description': product.description,
                                           'stock': product.stock,
                                           'price': product.price})
        self.uow.commit()
        return product

    def delete_product(self, product_id: str):
        self.uow.repository.delete(product_id)
        self.uow.commit()
