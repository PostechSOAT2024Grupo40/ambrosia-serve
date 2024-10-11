from uuid import uuid4

from pydantic import BaseModel, Field

from src.shared.enums.categories import Categories


class CreateProductRequestDto(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    description: str
    price: float
    stock: int
    category: Categories

    class Config:
        use_enum_values = True
