from typing import List

from src.api.presentation.shared.dtos.client_response_dto import ClientResponseDto
from src.client.domain.entities.user import User
from src.client.ports.users_presenter import IUserPresenter


class PydanticClientPresenter(IUserPresenter):
    def present(self, output: User | List[User]) -> ClientResponseDto | List[ClientResponseDto]:
        if isinstance(output, list):
            return [self.formater(user) for user in output]
        return self.formater(output)

    @staticmethod
    def formater(user):
        if not user:
            return {}
        return ClientResponseDto(id=user.id,
                                 first_name=user.first_name,
                                 last_name=user.last_name,
                                 cpf=user.cpf,
                                 email=user.email)
