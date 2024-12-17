from typing import Optional

from src.client.domain.entities.user import User
from src.client.ports.unit_of_work_interface import IClientUnitOfWork
from src.client.ports.user_gateway import IUserGateway


class PostgreSqlClientGateway(IUserGateway):
    def __init__(self, uow: IClientUnitOfWork):
        super().__init__()
        self.uow = uow

    def get_users(self) -> list[User]:
        with self.uow:
            users = self.uow.repository.get_users()
            return [self.build_user_entity(u) for u in users]

    def get_user_by_cpf(self, cpf: str) -> Optional[User]:
        with self.uow:
            user = self.uow.repository.get_user_by_cpf(cpf)
            if not user:
                return
            return self.build_user_entity(user)

    def get_user_by_email(self, email: str) -> Optional[User]:
        with self.uow:
            user = self.uow.repository.get_user_by_email(email)
            if not user:
                return
            return self.build_user_entity(user)

    def create_user(self, user: User) -> User:
        with self.uow:
            self.uow.repository.create_user({'id': user.id,
                                             'first_name': user.first_name,
                                             'last_name': user.last_name,
                                             'cpf': user.cpf,
                                             'email': user.email,
                                             'password': user.password})
            self.uow.commit()
            return user

    def update_user(self, user: User) -> User:
        with self.uow:
            self.uow.repository.update_user({'id': user.id,
                                             'first_name': user.first_name,
                                             'last_name': user.last_name,
                                             'cpf': user.cpf,
                                             'email': user.email,
                                             'password': user.password})
            self.uow.commit()
            return user

    def delete_user(self, user_id: str) -> bool:
        with self.uow:
            self.uow.repository.delete_user(user_id)
            self.uow.commit()
            return True

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        with self.uow:
            user = self.uow.repository.get_user_by_id(user_id)
            if not user:
                return
            return self.build_user_entity(user)

    @staticmethod
    def build_user_entity(user):
        if not user:
            return
        return User(_id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    cpf=user.cpf,
                    email=user.email,
                    password=user.password)
