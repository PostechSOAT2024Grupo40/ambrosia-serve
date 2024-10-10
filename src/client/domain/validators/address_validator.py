from src.client.domain.domain_exception import ClientDomainException


class AddressValidator:

    @staticmethod
    def validate(address):
        if not address.number.strip():
            raise ClientDomainException("Número de endereço não pode ser vazio")

        if not address.street.strip():
            raise ClientDomainException("Rua não pode ser vazia")
