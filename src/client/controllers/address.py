from typing import Dict

from src.client.ports.gateways.address_gateway import IAddressGateway
from src.client.ports.presenters.address_presenter import IAddressPresenter
from src.shared.repository_interface import IRepository
from src.client.use_cases import AddressUseCase


class AddressController:

    @staticmethod
    def create(request_data: Dict):
        repository: IRepository = ...
        gateway: IAddressGateway = ...
        presenter: IAddressPresenter = ...

        address = AddressUseCase.create_new_address(request_data=request_data, gateway=gateway)

        return presenter.present(address)

    @staticmethod
    def update(request_data: Dict):
        repository: IRepository = ...
        gateway: IAddressGateway = ...
        presenter: IAddressPresenter = ...

        address = AddressUseCase.update_address(request_data=request_data, gateway=gateway)

        return presenter.present(address)

    @staticmethod
    def delete(address_id: int):
        repository: IRepository = ...
        gateway: IAddressGateway = ...

        AddressUseCase.delete_address(address_id=address_id, gateway=gateway)

        return True

    @staticmethod
    def get_all():
        repository: IRepository = ...
        gateway: IAddressGateway = ...
        presenter: IAddressPresenter = ...

        address = AddressUseCase.get_addresses(gateway=gateway)

        return presenter.present(address)

    @staticmethod
    def get_by_id(address_id: int):
        repository: IRepository = ...
        gateway: IAddressGateway = ...
        presenter: IAddressPresenter = ...

        address = AddressUseCase.get_by_id(address_id=address_id, gateway=gateway)

        return presenter.present(address)
