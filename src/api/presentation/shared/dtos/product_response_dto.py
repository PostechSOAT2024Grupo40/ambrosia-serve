from typing import Optional

from pydantic import BaseModel


class ProductResponseDto(BaseModel):
    id: Optional[str] = ''
    sku: Optional[str] = ''
    description: Optional[str] = ''
    category: Optional[str] = ''
    stock: Optional[int] = None
    price: Optional[float] = None
