from src.client.domain.object_values import generate_id
from src.client.domain.validators.user_validator import UserValidator


class User:
    def __init__(self,

                 first_name: str,
                 last_name: str,
                 cpf: str,
                 email: str,
                 password: str,
                 _id: str = None):
        self._id = _id or generate_id()
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.email = email
        self.password = password

        UserValidator.validate_user(user=self)

    @property
    def id(self):
        return self._id

    def __hash__(self):
        return hash(self.cpf)

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.cpf == other.cpf
