from typing import Dict

from src.domain.entities.user import User
from src.ports.presenters.create_new_user_presenter import ICreateNewUserPresenter
from src.ports.repositories.user_repository import IUserRepository
from src.shared.dtos.create_user_dtos import InputCreateUserDTO


class CreateNewUserUserCase:
    def __init__(self, user_repository: IUserRepository, presenter: ICreateNewUserPresenter):
        self.user_repository = user_repository
        self.presenter = presenter

    def execute(self, input_dto: InputCreateUserDTO) -> Dict:
        try:
            user = User(first_name=input_dto.first_name,
                        last_name=input_dto.last_name,
                        cpf=input_dto.cpf,
                        email=input_dto.email,
                        password=input_dto.password,
                        address=input_dto.address)
            self.user_repository.create_user(user)
            self.presenter.present(user)
            return user.to_dict()
        except Exception:
            pass
