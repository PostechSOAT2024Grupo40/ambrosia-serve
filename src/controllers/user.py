from typing import Dict

from src.ports.gateways.user_gateway import IUserGateway
from src.ports.presenters.users_presenter import IUserPresenter
from src.ports.repository import IRepository
from src.use_cases.user import UsersUseCase


class UserController:

    @staticmethod
    def create_user(request_data: Dict):
        repository: IRepository = ...
        gateway: IUserGateway = ...
        presenter: IUserPresenter = ...
        user = UsersUseCase.create_new_user(request_data=request_data, gateway=gateway)
        return presenter.user_present(user)

    @staticmethod
    def get_users(self):
        repository: IRepository = ...
        gateway: IUserGateway = ...
        presenter: IUserPresenter = ...
        users = UsersUseCase.get_users(gateway=gateway)
        return presenter.user_present(users)

    @staticmethod
    def get_user_by_cpf(cpf: str):
        repository: IRepository = ...
        gateway: IUserGateway = ...
        presenter: IUserPresenter = ...
        user = UsersUseCase.get_user_by_cpf(cpf=cpf, gateway=gateway)
        return presenter.user_present(user)

    @staticmethod
    def update_user(request_data: Dict):
        repository: IRepository = ...
        gateway: IUserGateway = ...
        presenter: IUserPresenter = ...
        user = UsersUseCase.update_user(request_data=request_data, gateway=gateway)
        return presenter.user_present(user)

    @staticmethod
    def delete_user(user_id: int):
        repository: IRepository = ...
        gateway: IUserGateway = ...
        UsersUseCase.delete_user(user_id=user_id, gateway=gateway)
        return True
