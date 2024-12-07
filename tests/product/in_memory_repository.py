from typing import Dict

from src.product.ports.repository_interface import IProductRepository


class InMemoryProductRepository(IProductRepository):
    def __init__(self):
        self.data = {}

    def get_all(self):
        return [self.data] if self.data else []

    def filter_by_sku(self, sku: str):
        _all = self.get_all()
        if not _all:
            return

        return [p for p in _all if p.get('sku') == sku][0]

    def insert_update(self, values: Dict):
        self.data['id'] = values

    def delete(self, sku: str):
        self.data.pop(sku, None)
