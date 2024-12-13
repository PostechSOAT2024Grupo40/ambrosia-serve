from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Any]:
        ...

    @abstractmethod
    def filter_by_id(self, order_id: str) -> Any:
        ...

    @abstractmethod
    def insert_update(self, values: Dict[str, Any]):
        ...

    @abstractmethod
    def delete(self, order_id: str):
        ...

    @abstractmethod
    def get_order_products(self, order_id: str) -> List[Any]:
        ...
