
from pydantic import BaseModel

from src.cart.domain.enums.paymentConditions import PaymentConditions
from src.cart.domain.entities.order_product import OrderProduct
from src.api.presentation.shared.dtos.create_product_request_dto import CreateProductRequestDto

class OrderProductDto(BaseModel):
    product: CreateProductRequestDto
    quantity: int
    observation: str

class CreateOrderRequestDto(BaseModel):
    user_id: str
    payment_condition: PaymentConditions
    products: list[OrderProductDto]
    
    class Config:
        use_enum_values = True
    
