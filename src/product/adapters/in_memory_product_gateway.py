from src.product.domain.entities.product import Product
from src.product.ports.product_gateway import IProductGateway
from src.shared.dtos.repository_params_dto import RepositoryParamsDTO
from src.shared.unit_of_work_interface import IUnitOfWork


class InMemoryProductGateway(IProductGateway):
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def get_products(self):
        return self.uow.repository.get_all('products')

    def get_product_by_id(self, product_id: int):
        results = self.uow.repository.filter_by('products',
                                                [RepositoryParamsDTO(key='id', value=str(product_id))])
        if not results:
            return
        return results[0]

    def create_update_product(self, product: Product):
        self.uow.repository.insert_update('products', [
            RepositoryParamsDTO(key='id', value=str(product.id)),
            RepositoryParamsDTO(key='category', value=product.category),
            RepositoryParamsDTO(key='description', value=product.description),
            RepositoryParamsDTO(key='stock', value=product.stock),
            RepositoryParamsDTO(key='price', value=str(product.price))
        ])
        self.uow.commit()
        return product

    def delete_product(self, product_id: int):
        self.uow.repository.delete('products',
                                   [RepositoryParamsDTO(key='id', value=str(product_id))])
        self.uow.commit()
