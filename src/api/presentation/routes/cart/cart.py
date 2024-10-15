from fastapi import APIRouter
from src.cart.cart_controller import CartController
from src.api.presentation.shared.dtos.create_order_request_dto import CreateOrderRequestDto

router = APIRouter()

@router.post("/api/v1/order")
async def create_order(order_request: CreateOrderRequestDto):
    order_request_dict = order_request.dict()
    return CartController.create_order(request_data=order_request_dict)

@router.get("/api/v1/orders")
async def get_all_orders():
    return CartController.get_orders()

@router.get("/api/v1/order/{id}")
async def get_order_by_id(id: str):
    return CartController.get_order_by_id(id)

@router.put("/api/v1/order/{id}")
async def update_order(id: str, order_request: CreateOrderRequestDto):
    order_request_dict = order_request.dict()
    return CartController.update_order(order_id=id, request_data=order_request_dict)

@router.put("/api/v1/order/{id}/status")
async def update_order_status(id: str, new_status: str):
    return CartController.update_order_status(order_id=id, new_status=new_status)

@router.delete("/api/v1/order/{id}")
async def delete_order(id: str):
    return CartController.delete_order(order_id=id)