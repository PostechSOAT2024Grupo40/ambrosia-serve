from abc import ABC, abstractmethod

from src.product.ports.repository_interface import IRepository


class IProductUnitOfWork(ABC):
    repository: IRepository

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
