from src.domain.domain_exception import DomainException


class AddressValidator:

    @staticmethod
    def validate(address):
        if not address.number.strip():
            raise DomainException("Número de endereço não pode ser vazio")

        if not address.street.strip():
            raise DomainException("Rua não pode ser vazia")
