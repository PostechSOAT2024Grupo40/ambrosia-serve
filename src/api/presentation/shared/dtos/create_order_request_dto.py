from typing import Optional

from pydantic import BaseModel

from src.cart.domain.enums.paymentConditions import PaymentConditions


class OrderProductDto(BaseModel):
    product_id: str
    quantity: int
    observation: Optional[str] = ''


class CreateOrderRequestDto(BaseModel):
    user_id: str
    payment_condition: PaymentConditions
    products: list[OrderProductDto]

    class Config:
        use_enum_values = True
