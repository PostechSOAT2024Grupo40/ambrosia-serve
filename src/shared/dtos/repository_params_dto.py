from dataclasses import dataclass


@dataclass
class RepositoryParamsDTO:
    key: str
    operator: str
    value: str
