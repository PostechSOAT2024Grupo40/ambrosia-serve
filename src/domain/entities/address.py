import uuid

from src.domain.validators.address_validator import AddressValidator


class Address:
    def __init__(self,
                 street: str,
                 number: str,
                 complement: str):
        self.id = str(uuid.uuid4())
        self.street = street
        self.number = number
        self.complement = complement

        AddressValidator.validate(address=self)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
