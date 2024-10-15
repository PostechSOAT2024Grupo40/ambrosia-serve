from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import ValidationError

from src.api.presentation.shared.dtos.client_response_dto import ClientResponseDto
from src.api.presentation.shared.dtos.create_user_request_dtos import CreateUserRequestDTO
from src.client.user_controller import UserController

router = APIRouter()


@router.post("/api/v1/user")
async def create_user(create_user: CreateUserRequestDTO) -> ClientResponseDto:
    try:
        create_user_dict = create_user.model_dump()
        return UserController.create_user(request_data=create_user_dict)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {create_user=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.get("/api/v1/users")
async def get_users() -> list[ClientResponseDto]:
    try:
        return UserController.get_users()
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception("Server Error")
        raise HTTPException(status_code=500, detail=exc.args)


@router.get("/api/v1/user/{cpf}")
async def get_user_by_cpf(cpf: str) -> ClientResponseDto:
    try:
        return UserController.get_user_by_cpf(cpf)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {cpf=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.put("/api/v1/user/")
async def update_user(update_user: CreateUserRequestDTO) -> ClientResponseDto:
    try:
        return UserController.update_user(update_user.model_dump())
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {update_user=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.delete("/api/v1/user/{id}")
async def delete_user(id: str) -> bool:
    try:
        return UserController.delete_user(id)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception(f"Server Error | {id=}")
        raise HTTPException(status_code=500, detail=exc.args)
