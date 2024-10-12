from src.product.product_controller import ProductController
from src.shared.dtos.create_product_request_dto import CreateProductRequestDto
from src.shared.enums.categories import Categories


def main():
    request = CreateProductRequestDto(
        sku="123456",
        description="Produto 1",
        price=10.00,
        stock=100,
        category=Categories.LANCHE
    )
    request_2 = CreateProductRequestDto(
        sku="12345600",
        description="Produto atualizado",
        price=10.00,
        stock=100,
        category=Categories.LANCHE
    )

    print(f"create: {ProductController.create_product(request_data=request.model_dump())=}")
    print(f"get by: {ProductController.get_product_by_id('21031576667768127252')}")
    print(f"get all: {ProductController.get_products()}")
    print(f"delete: {ProductController.delete_product('21031576667768127252')}")
    print(f"update: {ProductController.update_product('21031576667768127252', request_2.model_dump())}")


if __name__ == "__main__":
    main()
