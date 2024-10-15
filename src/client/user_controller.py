from typing import Dict

from src.client.adapters.postgres_gateway import PostgreSqlClientGateway
from src.client.adapters.postgresql_uow import ClientPostgreSqlUow
from src.client.adapters.pydantic_presenter import PydanticClientPresenter
from src.client.ports.unit_of_work_interface import IClientUnitOfWork
from src.client.ports.user_gateway import IUserGateway
from src.client.ports.users_presenter import IUserPresenter
from src.client.use_cases.user import UsersUseCase
from src.shared.postgresql_session_factory import postgresql_session_factory


class UserController:

    @staticmethod
    def create_user(request_data: Dict):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        user = UsersUseCase.create_new_user(request_data=request_data, gateway=gateway)
        return presenter.present(user)

    @staticmethod
    def get_users():
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        users = UsersUseCase.get_users(gateway=gateway)
        return presenter.present(users)

    @staticmethod
    def get_user_by_cpf(cpf: str):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        user = UsersUseCase.get_user_by_cpf(cpf=cpf, gateway=gateway)
        return presenter.present(user)

    @staticmethod
    def update_user(request_data: Dict):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        user = UsersUseCase.update_user(request_data=request_data, gateway=gateway)
        return presenter.present(user)

    @staticmethod
    def delete_user(user_id: int):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        UsersUseCase.delete_user(user_id=user_id, gateway=gateway)
        return True
