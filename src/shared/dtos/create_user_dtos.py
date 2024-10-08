from pydantic.dataclasses import dataclass


@dataclass
class InputCreateUserDTO:
    first_name: str
    last_name: str
    cpf: str
    email: str
    password: str
    address: list


@dataclass
class OutputCreateUserDTO:
    id: str
