from typing import List, Dict

from src.product.domain.entities.product import Product
from src.product.ports.product_presenter import IProductPresenter


class JsonProductPresenter(IProductPresenter):
    def present(self, output: Product | List[Product]) -> Dict[str, str] | List[Dict[str, str]]:
        if isinstance(output, list):
            return [self.formater(p) for p in output]
        return self.formater(output)

    @staticmethod
    def formater(p):
        if not p:
            return {}
        return {
            "id": p.id,
            "sku": p.sku,
            "description": p.description,
            "category": p.category,
            "stock": p.stock,
            "price": p.price
        }
