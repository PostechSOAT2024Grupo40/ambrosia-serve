from typing import Optional

from pydantic import BaseModel


class ProductResponseDto(BaseModel):
    id: Optional[str] = ''
    name: Optional[str] = ''
    description: Optional[str] = ''
    category: Optional[str] = ''
    stock: Optional[int] = None
    price: Optional[float] = None
