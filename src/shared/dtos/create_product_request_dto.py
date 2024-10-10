import decimal
from uuid import uuid4

from pydantic import BaseModel,  Field

from src.shared.enums.categories import Categories


class CreateProductRequestDto(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    description: str
    price: decimal.Decimal
    stock: int
    category: Categories
