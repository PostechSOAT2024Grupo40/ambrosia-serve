from src.product.product_controller import ProductController
from src.shared.dtos.create_product_request_dto import CreateProductRequestDto
from src.shared.enums.categories import Categories


def main():
    request = CreateProductRequestDto(
        description="Produto 1",
        price=10.00,
        stock=100,
        category=Categories.LANCHE
    )
    response = ProductController.create_product(request_data=request.model_dump())
    print(f"{response=}")


if __name__ == "__main__":
    main()
