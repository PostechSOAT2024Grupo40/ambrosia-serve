from abc import ABC, abstractmethod
from typing import List, Optional

from src.client.domain.entities.address import Address


class IAddressGateway(ABC):

    @abstractmethod
    def insert_address(self, address: Address) -> Address:
        ...

    @abstractmethod
    def get_all(self) -> List[Address]:
        ...

    @abstractmethod
    def get_by_id(self, address_id: int) -> Optional[Address]:
        ...

    @abstractmethod
    def update(self, address: Address) -> Address:
        ...

    @abstractmethod
    def delete(self, address_id: int) -> None:
        ...
