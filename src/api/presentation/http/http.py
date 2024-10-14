from fastapi import FastAPI
from src.api.presentation.routes.products import products
from src.api.presentation.routes.cart import cart
from src.api.presentation.routes.client import client

app = FastAPI()
app.include_router(products.router, tags=["products"])
app.include_router(client.router, tags=["users"])
app.include_router(cart.router, tags=["cart"])
