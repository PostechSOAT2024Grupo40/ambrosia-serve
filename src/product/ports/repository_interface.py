from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IProductRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Any]:
        ...

    @abstractmethod
    def filter_by_sku(self, sku: str) -> Any:
        ...

    @abstractmethod
    def insert_update(self, values: Dict[str, Any]):
        ...

    @abstractmethod
    def delete(self, sku: str):
        ...
