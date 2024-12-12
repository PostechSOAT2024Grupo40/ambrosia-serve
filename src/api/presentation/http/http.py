from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.presentation.routes.cart import cart
from src.api.presentation.routes.client import client
from src.api.presentation.routes.health import health
from src.api.presentation.routes.products import products
from src.cart.adapters.order_table import Base as OrderBase
from src.client.adapters.client_table import Base as ClientBase
from src.product.adapters.product_table import Base as ProductBase
from src.shared.postgresql_session_factory import get_db_url


@asynccontextmanager
async def lifespan(app: FastAPI):
    all_bases = [ProductBase, ClientBase, OrderBase]
    for base in all_bases:
        base.metadata.create_all(get_db_url(), checkfirst=True)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(products.router, tags=["products"])
app.include_router(client.router, tags=["users"])
app.include_router(cart.router, tags=["cart"])

app.include_router(health.router, tags=["health"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
