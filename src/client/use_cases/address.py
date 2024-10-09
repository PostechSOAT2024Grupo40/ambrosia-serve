from typing import Any, Dict, Optional, List

from src.client.domain.entities.address import Address
from src.client.ports.gateways.address_gateway import IAddressGateway
from src.client.exceptions import AddressNotFoundError, AddressExistsError


class AddressUseCase:
    @staticmethod
    def create_new_address(request_data: Dict, gateway: IAddressGateway) -> Any:
        if AddressUseCase.get_by_id(address_id=request_data["id"], gateway=gateway):
            raise AddressExistsError(address=request_data["id"])

        address = Address(street=request_data["street"],
                          number=request_data["number"],
                          complement=request_data.get("complement"))

        return gateway.insert_address(address)

    @staticmethod
    def update_address(request_data: Dict, gateway: IAddressGateway) -> Any:
        if not AddressUseCase.get_by_id(address_id=request_data["id"], gateway=gateway):
            raise AddressNotFoundError(address=request_data["id"])

        address = Address(street=request_data["street"],
                          number=request_data["number"],
                          complement=request_data.get("complement"))

        return gateway.update(address)

    @staticmethod
    def delete_address(address_id: int, gateway: IAddressGateway):
        address = gateway.get_by_id(address_id=address_id)
        if not address:
            raise AddressNotFoundError(address=address_id)

        gateway.delete(address.id)

    @staticmethod
    def get_by_id(address_id: int, gateway: IAddressGateway) -> Optional[Address]:
        return gateway.get_by_id(address_id=address_id)

    @staticmethod
    def get_addresses(gateway: IAddressGateway) -> List[Address]:
        return gateway.get_all()
