from abc import ABC, abstractmethod
from typing import List

from src.cart.domain.entities.order import Order
from src.cart.ports.unit_of_work_interface import ICartUnitOfWork


class ICartGateway(ABC):
    uow: ICartUnitOfWork

    @abstractmethod
    def get_orders(self) -> List[Order]:
        ...

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> Order:
        ...

    @abstractmethod
    def create_update_order(self, order: Order) -> Order:
        ...

    @abstractmethod
    def delete_order(self, order_id: str) -> None:
        ...
