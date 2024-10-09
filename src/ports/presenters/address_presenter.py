from abc import ABC, abstractmethod
from typing import List, Any

from src.domain.entities.address import Address


class IAddressPresenter(ABC):

    @abstractmethod
    def present(self, output: Address | List[Address]) -> Any:
        ...
