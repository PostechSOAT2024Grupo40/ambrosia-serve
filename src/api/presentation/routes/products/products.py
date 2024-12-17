from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import ValidationError

from src.api.presentation.shared.dtos.create_product_request_dto import CreateProductRequestDto
from src.api.presentation.shared.dtos.product_response_dto import ProductResponseDto
from src.product.domain_exception import ProductDomainException
from src.product.exceptions import ProductExistsError, ProductNotFoundError
from src.product.product_controller import ProductController

router = APIRouter()


@router.post("/api/v1/product")
async def create_product(product: CreateProductRequestDto) -> ProductResponseDto:
    try:
        product_dict = product.model_dump()
        return ProductController.create_product(request_data=product_dict)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except (ProductDomainException, ProductExistsError, ProductNotFoundError) as domain_exc:
        logger.exception(f"Server Error | {product=}")
        raise HTTPException(status_code=409, detail=domain_exc.args)
    except Exception as exc:
        logger.exception(f"Server Error | {product=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.get("/api/v1/product/{_id}")
async def get_product_by_id(_id: str):
    try:
        return ProductController.get_product_by_id(_id)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except (ProductDomainException, ProductExistsError, ProductNotFoundError) as domain_exc:
        logger.exception(f"Server Error | {_id=}")
        raise HTTPException(status_code=409, detail=domain_exc.args)
    except Exception as exc:
        logger.exception(f"Server Error | {_id=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.get("/api/v1/products")
async def get_all_products():
    try:
        return ProductController.get_products()
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except Exception as exc:
        logger.exception("Server Error")
        raise HTTPException(status_code=500, detail=exc.args)


@router.delete("/api/v1/product/{_id}")
async def delete_product(_id: str):
    try:
        return ProductController.delete_product(_id)
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except (ProductDomainException, ProductNotFoundError) as domain_exc:
        logger.exception(f"Server Error | {_id=}")
        raise HTTPException(status_code=409, detail=domain_exc.args)
    except Exception as exc:
        logger.exception(f"Server Error | {_id=}")
        raise HTTPException(status_code=500, detail=exc.args)


@router.put("/api/v1/product/{_id}")
async def update_product(_id: str, payload: CreateProductRequestDto):
    try:
        return ProductController.update_product(product_id=_id, request_data=payload.model_dump())
    except ValidationError as pydantic_exc:
        raise HTTPException(status_code=400, detail=pydantic_exc.errors())
    except (ProductDomainException, ProductExistsError, ProductNotFoundError) as domain_exc:
        logger.exception(f"Server Error | {_id=} {payload=}")
        raise HTTPException(status_code=409, detail=domain_exc.args)
    except Exception as exc:
        logger.exception(f"Server Error | {_id=} {payload=}")
        raise HTTPException(status_code=500, detail=exc.args)
