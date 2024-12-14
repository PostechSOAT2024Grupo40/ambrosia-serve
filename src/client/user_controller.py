from typing import Dict

from src.client.adapters.postgres_gateway import PostgreSqlClientGateway
from src.client.adapters.postgresql_uow import ClientPostgreSqlUow
from src.client.adapters.pydantic_presenter import PydanticClientPresenter
from src.client.ports.unit_of_work_interface import IClientUnitOfWork
from src.client.ports.user_gateway import IUserGateway
from src.client.ports.users_presenter import IUserPresenter
from src.client.use_cases.create_use import CreateUserUseCase
from src.client.use_cases.delete_user import DeleteUserUseCase
from src.client.use_cases.get_all_users import GetAllUsersUseCase
from src.client.use_cases.get_user_by_cpf import GetUserByCpfUseCase
from src.client.use_cases.update_user import UpdateUserUseCase
from src.shared.postgresql_session_factory import postgresql_session_factory


class UserController:

    @staticmethod
    def create_user(request_data: Dict):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        create_user_usecase = CreateUserUseCase(gateway=gateway)
        user = create_user_usecase.execute(request_data=request_data)
        return presenter.present(user)

    @staticmethod
    def get_users():
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        get_all_uses_usecase = GetAllUsersUseCase(gateway=gateway)
        users = get_all_uses_usecase.execute()
        return presenter.present(users)

    @staticmethod
    def get_user_by_cpf(cpf: str):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        get_user_by_cpf_usecase = GetUserByCpfUseCase(gateway=gateway)
        user = get_user_by_cpf_usecase.execute(cpf=cpf)
        return presenter.present(user)

    @staticmethod
    def update_user(request_data: Dict):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        presenter: IUserPresenter = PydanticClientPresenter()
        update_user_usecase = UpdateUserUseCase(gateway=gateway)
        user = update_user_usecase.execute(request_data=request_data)
        return presenter.present(user)

    @staticmethod
    def delete_user(user_id: str):
        uow: IClientUnitOfWork = ClientPostgreSqlUow(session_factory=postgresql_session_factory())
        gateway: IUserGateway = PostgreSqlClientGateway(uow)
        delete_user_usecase = DeleteUserUseCase(gateway=gateway)
        delete_user_usecase.execute(user_id=user_id)
        return True
