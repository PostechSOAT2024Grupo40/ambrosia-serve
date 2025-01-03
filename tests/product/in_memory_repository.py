from typing import Dict, Any

from src.product.ports.repository_interface import IProductRepository


class InMemoryProductRepository(IProductRepository):

    def __init__(self):
        self.data = {}

    def get_all(self):
        return [self.data] if self.data else []

    def find_by_name(self, name: str) -> Any:
        _all = self.get_all()
        if not _all:
            return
        return [p for p in _all if p.get('name') == name][0]

    def filter_by_id(self, product_id: str):
        _all = self.get_all()
        if not _all:
            return

        return [p for p in _all if p.get('id') == product_id][0]

    def insert_update(self, values: Dict):
        self.data['id'] = values

    def delete(self, product_id: str):
        self.data.pop(product_id, None)
