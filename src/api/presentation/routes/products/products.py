from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from src.api.presentation.shared.dtos.create_product_request_dto import CreateProductRequestDto
from src.api.presentation.shared.dtos.product_response_dto import ProductResponseDto
from src.product.product_controller import ProductController

router = APIRouter()


@router.post("/api/v1/product")
async def create_product(product: CreateProductRequestDto) -> ProductResponseDto:
    try:
        product_dict = product.model_dump()
        return ProductController.create_product(request_data=product_dict)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Server Error")


@router.get("/api/v1/product/{sku}")
async def get_product_by_id(sku: str):
    try:
        return ProductController.get_product_by_id(sku)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Server Error")


@router.get("/api/v1/products")
async def get_all_products():
    try:
        return ProductController.get_products()
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete("/api/v1/product/{sku}")
async def delete_product(sku: str):
    try:
        return ProductController.delete_product(sku)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Server Error")


@router.put("/api/v1/product/{sku}")
async def update_product(sku: str, update_product: CreateProductRequestDto):
    try:
        return ProductController.update_product(sku=sku, request_data=update_product)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Server Error")
