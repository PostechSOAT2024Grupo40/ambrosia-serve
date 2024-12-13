from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IProductRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Any]:
        ...

    @abstractmethod
    def filter_by_id(self, product_id: str) -> Any:
        ...

    @abstractmethod
    def insert_update(self, values: Dict[str, Any]):
        ...

    @abstractmethod
    def delete(self, product_id: str):
        ...

    @abstractmethod
    def find_by_name(self, name: str) -> Any:
        ...
