from src.product.exceptions import ProductNotFoundError
from src.product.ports.product_gateway import IProductGateway


class DeleteProductUseCase:
    def __init__(self, gateway: IProductGateway):
        self.gateway = gateway

    def execute(self, product_id: str) -> None:
        product_ = self.gateway.get_product_by_id(product_id=product_id)
        if not product_:
            raise ProductNotFoundError(product=product_id)

        self.gateway.delete_product(product_id)
