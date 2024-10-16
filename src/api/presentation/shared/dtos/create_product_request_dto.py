from pydantic import BaseModel

from src.api.presentation.shared.enums.categories import Categories


class CreateProductRequestDto(BaseModel):
    sku: str
    description: str
    price: float
    stock: int
    category: Categories

    class Config:
        use_enum_values = True
