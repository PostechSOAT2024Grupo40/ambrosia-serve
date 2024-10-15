from typing import Optional, List

from pydantic import BaseModel


class OrderProductResponseDto(BaseModel):
    product: str
    quantity: int
    observation: Optional[str] = ''


class OrderResponseDto(BaseModel):
    id: str
    user: int
    total_order: float
    order_status: str
    payment_condition: str
    products: List[OrderProductResponseDto]
