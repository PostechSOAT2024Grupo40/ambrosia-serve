from typing import Optional

from pydantic import BaseModel


class ClientResponseDto(BaseModel):
    id: Optional[str] = ''
    first_name: Optional[str] = ''
    last_name: Optional[str] = ''
    cpf: Optional[str] = ''
    email: Optional[str] = ''
