from abc import ABC, abstractmethod
from typing import List, Dict


class IClientRepository(ABC):

    @abstractmethod
    def get_users(self) -> List[Dict]:
        ...

    @abstractmethod
    def get_user_by_cpf(self, cpf: str) -> Dict:
        ...

    @abstractmethod
    def get_user_by_email(self, email: str) -> Dict:
        ...

    @abstractmethod
    def create_user(self, user: Dict):
        ...

    @abstractmethod
    def update_user(self, user: Dict):
        ...

    @abstractmethod
    def delete_user(self, user_id: int):
        ...

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Dict:
        ...
