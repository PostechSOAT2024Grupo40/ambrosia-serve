from fastapi import APIRouter
from src.product.product_controller import ProductController
from src.shared.dtos.create_product_request_dto import CreateProductRequestDto

router = APIRouter()

@router.post("/api/v1/product")
async def create_product(product: CreateProductRequestDto):
    product_dict = product.dict()
    return ProductController.create_product(request_data=product_dict)

@router.get("/api/v1/product/{sku}")
async def get_product_by_id(sku: str):
    return ProductController.get_product_by_id(sku)

@router.get("/api/v1/products")
async def get_all_products():
    return ProductController.get_products()

@router.delete("/api/v1/product/{sku}")
async def delete_product(sku: str):
    return ProductController.delete_product(sku)

@router.put("/api/v1/product/{sku}")
async def update_product(sku: str, updateProduct: CreateProductRequestDto):
    return ProductController.update_product(sku=sku, request_data=updateProduct)
