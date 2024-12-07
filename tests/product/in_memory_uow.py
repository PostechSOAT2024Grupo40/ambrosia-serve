from src.product.ports.repository_interface import IProductRepository
from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class InMemoryUow(IProductUnitOfWork):
    def __init__(self, repository: IProductRepository):
        self.repository = repository
        self._committed = False

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def commit(self):
        self._committed = True

    def rollback(self):
        pass