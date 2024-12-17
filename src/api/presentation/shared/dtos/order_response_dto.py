from typing import Optional

from pydantic import BaseModel

from src.api.presentation.shared.enums.status import OrderStatus


class OrderProductResponseDto(BaseModel):
    product: str
    quantity: int
    observation: Optional[str] = ''


class OrderResponseDto(BaseModel):
    id: str
    user: str
    total_order: float
    order_status: OrderStatus
    payment_condition: str
    products: list[OrderProductResponseDto]
