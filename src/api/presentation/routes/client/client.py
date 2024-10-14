from fastapi import APIRouter
from src.api.presentation.shared.dtos.create_user_request_dtos import CreateUserRequestDTO
from src.client.user_controller import UserController

router = APIRouter()

@router.post("/api/v1/user")
async def create_user(create_user: CreateUserRequestDTO):
    create_user_dict = create_user.dict()
    return UserController.create_user(request_data=create_user_dict)

@router.get("/api/v1/users")
async def get_users():
    return UserController.get_users()

@router.get("/api/v1/user/{cpf}")
async def get_user_by_cpf(cpf: str):
    return UserController.get_user_by_cpf(cpf)

@router.put("/api/v1/user/")
async def update_user(update_user: CreateUserRequestDTO):
    return UserController.update_user(update_user)

@router.delete("/api/v1/user/{id}")
async def delete_user(id: str):
    return UserController.delete_user(id)