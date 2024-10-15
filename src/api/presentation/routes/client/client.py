from fastapi import APIRouter

from src.api.presentation.shared.dtos.client_response_dto import ClientResponseDto
from src.api.presentation.shared.dtos.create_user_request_dtos import CreateUserRequestDTO
from src.client.user_controller import UserController

router = APIRouter()


@router.post("/api/v1/user")
async def create_user(create_user: CreateUserRequestDTO) -> ClientResponseDto:
    create_user_dict = create_user.dict()
    return UserController.create_user(request_data=create_user_dict)


@router.get("/api/v1/users")
async def get_users() -> list[ClientResponseDto]:
    return UserController.get_users()


@router.get("/api/v1/user/{cpf}")
async def get_user_by_cpf(cpf: str) -> ClientResponseDto:
    return UserController.get_user_by_cpf(cpf)


@router.put("/api/v1/user/")
async def update_user(update_user: CreateUserRequestDTO) -> ClientResponseDto:
    return UserController.update_user(update_user)


@router.delete("/api/v1/user/{id}")
async def delete_user(id: str) -> bool:
    return UserController.delete_user(id)
