from abc import ABC, abstractmethod
from typing import List

from src.shared.dtos.repository_params_dto import RepositoryParamsDTO


class IRepository(ABC):
    """
    Repository interface definition for all repositories.
    """

    @abstractmethod
    def get_all(self, table_name: str):
        ...

    @abstractmethod
    def filter_by(self, table_name: str, params: List[RepositoryParamsDTO]):
        ...

    @abstractmethod
    def insert_update(self, table_name: str, params: List[RepositoryParamsDTO]):
        ...

    @abstractmethod
    def delete(self, table_name: str, params: List[RepositoryParamsDTO]):
        ...
