from typing import Annotated, Optional

from pydantic import BaseModel, Field

from src.api.presentation.shared.enums.categories import Categories


class CreateProductRequestDto(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: Categories
    image: Annotated[Optional[str], Field(description="URL/Diretório da imagem do produto")] = ""

    class Config:
        use_enum_values = True
