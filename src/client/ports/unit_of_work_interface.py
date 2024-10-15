from abc import ABC, abstractmethod

from src.client.ports.repository_interface import IClientRepository


class IClientUnitOfWork(ABC):
    repository: IClientRepository

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
