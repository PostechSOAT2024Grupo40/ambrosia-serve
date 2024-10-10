from pydantic import BaseModel, EmailStr


class CreateUserRequestDTO(BaseModel):
    first_name: str
    last_name: str
    cpf: str
    email: EmailStr
    password: str
