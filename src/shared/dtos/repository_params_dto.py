from dataclasses import dataclass
from typing import Any


@dataclass
class RepositoryParamsDTO:
    key: str
    value: Any
