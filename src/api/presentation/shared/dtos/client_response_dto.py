from typing import Optional

from pydantic import BaseModel


class ClientResponseDto(BaseModel):
    id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[str] = None
