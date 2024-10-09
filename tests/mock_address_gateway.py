from typing import List, Dict, Optional

from src.client.domain.entities.address import Address
from src.client.exceptions import AddressExistsError, AddressNotFoundError
from src.client.ports.gateways.address_gateway import IAddressGateway


class MockAddressGateway(IAddressGateway):
    def __init__(self):
        self.address_by_id: Dict[str, Address] = {}

    def get_all(self) -> List[Address]:
        return list(self.address_by_id.values())

    def get_by_id(self, address_id: int) -> Optional[Address]:
        return self.address_by_id.get(str(address_id))

    def insert_address(self, address: Address) -> Address:
        if address.id in self.address_by_id:
            raise AddressExistsError(address=address.id)
        self.address_by_id[address.id] = address
        return address

    def update(self, address: Address) -> Address:
        if address.id not in self.address_by_id:
            raise AddressNotFoundError(address=address.id)
        self.address_by_id[address.id] = address
        return address

    def delete(self, address_id: int) -> None:
        address = self.address_by_id.pop(str(address_id), None)
        if address:
            self.address_by_id.pop(address.id, None)
