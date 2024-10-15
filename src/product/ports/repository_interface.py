from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IProductRepository(ABC):
    """
    Repository interface definition for all repositories.
    """

    @abstractmethod
    def get_all(self) -> List[Dict]:
        ...

    @abstractmethod
    def filter_by_sku(self, sku: str) -> Dict:
        ...

    @abstractmethod
    def insert_update(self, values: Dict[str, Any]) -> Dict:
        ...

    @abstractmethod
    def delete(self, sku: str) -> bool:
        ...
