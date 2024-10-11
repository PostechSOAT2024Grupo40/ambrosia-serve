from typing import Dict

from src.product.domain.object_value import sku
from src.product.ports.repository_interface import IRepository


class InMemoryRepository(IRepository):
    def __init__(self):
        self.data = {}

    def get_all(self):
        return [self.data] if self.data else []

    def filter_by_sku(self, sku: str):
        return self.data.get(sku, None)

    def insert_update(self, values: Dict):
        self.data[sku] = values

    def delete(self, sku: str):
        self.data.pop(sku, None)
