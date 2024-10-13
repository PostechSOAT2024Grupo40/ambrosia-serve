class OrderExistsError(Exception):
    def __init__(self, order):
        super().__init__(f"O pedido {order} ja existe")


class OrderNotFoundError(Exception):
    def __init__(self, order):
        super().__init__(f"O pedido {order} não existe")


class OrderPaymentError(Exception):
    def __init__(self, order, payment):
        super().__init__(f"O pagamento {payment} para o pedido {order} é inválido")


class OrderPaymentExpiredError(Exception):
    def __init__(self, order):
        super().__init__(f"O pedido {order} expirou")


class ClientError(Exception):
    def __init__(self, client):
        super().__init__(f"O cliente {client} do pedido não foi localizado")


class ProductNotFoundError(Exception):
    def __init__(self, product):
        super().__init__(f"O produto {product} nao existe")
