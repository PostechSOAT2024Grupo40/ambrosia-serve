class OrderDomainException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class OrderProductDomainException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
