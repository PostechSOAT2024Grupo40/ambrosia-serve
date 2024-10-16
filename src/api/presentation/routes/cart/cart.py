from typing import List

from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import ValidationError

from src.api.presentation.shared.dtos.create_order_request_dto import CreateOrderRequestDto
from src.api.presentation.shared.dtos.order_response_dto import OrderResponseDto
from src.cart.cart_controller import CartController

router = APIRouter()


@router.post("/api/v1/order")
async def create_order(order_request: CreateOrderRequestDto) -> OrderResponseDto:
    try:
        order_request_dict = order_request.model_dump()
        return CartController.create_order(request_data=order_request_dict)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {order_request=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.get("/api/v1/orders")
async def get_all_orders() -> List[OrderResponseDto]:
    try:
        return CartController.get_orders()
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception("Server Error")
        raise HTTPException(status_code=500, detail=exc.args)


@router.get("/api/v1/order/{id}")
async def get_order_by_id(id: str) -> OrderResponseDto:
    try:
        return CartController.get_order_by_id(id)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {id=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.put("/api/v1/order/{id}/status")
async def update_order_status(id: str, new_status: str) -> OrderResponseDto:
    try:
        return CartController.update_order_status(order_id=id, new_status=new_status)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {id=} {new_status=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.delete("/api/v1/order/{id}")
async def delete_order(id: str):
    try:
        return CartController.delete_order(order_id=id)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {id=}")
        raise HTTPException(status_code=500, detail=exc.args)
