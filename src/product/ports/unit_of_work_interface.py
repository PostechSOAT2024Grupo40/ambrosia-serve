from abc import ABC, abstractmethod

from product.ports.repository_interface import IProductRepository


class IProductUnitOfWork(ABC):

    @abstractmethod
    def __enter__(self):
        ...

    @abstractmethod
    def __exit__(self, *args):
        ...

    @abstractmethod
    def commit(self):
        ...

    @abstractmethod
    def rollback(self):
        pass
