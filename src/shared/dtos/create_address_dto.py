from typing import Optional

from pydantic import BaseModel


class CreateAddressDto(BaseModel):
    street: str
    number: str
    complement: Optional[str] = None
