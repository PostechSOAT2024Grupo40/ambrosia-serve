from fastapi import FastAPI

from src.api.presentation.routes.cart import cart
from src.api.presentation.routes.client import client
from src.api.presentation.routes.health import health
from src.api.presentation.routes.products import products
from src.shared.postgresql_session_factory import create_db

app = FastAPI()
app.include_router(products.router, tags=["products"])
app.include_router(client.router, tags=["users"])
app.include_router(cart.router, tags=["cart"])

app.include_router(health.router, tags=["health"])

if __name__ == "__main__":
    import uvicorn

    create_db()
    uvicorn.run("app", host="0.0.0.0", port=8000, reload=True)
