from typing import Optional

from pydantic import BaseModel


class ProductResponseDto(BaseModel):
    id: Optional[str] = None
    sku: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    stock: Optional[int] = None
    price: Optional[float] = None
