from fastapi import FastAPI
from src.api.presentation.routes.products import products

app = FastAPI()

app.include_router(products.router)
