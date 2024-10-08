from abc import ABC
from typing import Dict

from src.shared.dtos.create_user_dtos import OutputCreateUserDTO


class ICreateNewUserPresenter(ABC):

    def present(self, output: OutputCreateUserDTO) -> Dict:
        raise NotImplementedError
