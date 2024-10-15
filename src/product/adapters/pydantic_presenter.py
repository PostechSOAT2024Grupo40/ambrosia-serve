from typing import List

from src.api.presentation.shared.dtos.product_response_dto import ProductResponseDto
from src.product.domain.entities.product import Product
from src.product.ports.product_presenter import IProductPresenter


class PydanticProductPresenter(IProductPresenter):
    def present(self, output: Product | List[Product]) -> ProductResponseDto | List[ProductResponseDto]:
        if isinstance(output, list):
            return [self.formater(p) for p in output]
        return self.formater(output)

    @staticmethod
    def formater(p):
        if not p:
            return {}
        return ProductResponseDto(id=p.id,
                                  sku=p.sku,
                                  description=p.description,
                                  category=p.category,
                                  stock=int(p.stock),
                                  price=float(p.price))
