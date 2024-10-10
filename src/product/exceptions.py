class ProductExistsError(Exception):
    def __init__(self, product):
        super().__init__(f"O produto {product} ja existe")


class ProductNotFoundError(Exception):
    def __init__(self, product):
        super().__init__(f"O produto {product} não existe")
