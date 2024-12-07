from typing import Any

from sqlalchemy import Integer, Column, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.functions import now

Base = declarative_base()


class ProductTable(Base):
    __tablename__ = "products"

    id = Column(String(255), primary_key=True,
                nullable=False, autoincrement=False)
    sku = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=now())
    updated_at = Column(DateTime, nullable=False,
                        default=now(), onupdate=now())

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.sku = kwargs.get('sku')
        self.description = kwargs.get('description')
        self.price = kwargs.get('price')
        self.stock = kwargs.get('stock')
        self.category = kwargs.get('category')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"ProductTable(id={self.id!r}, "
                f"sku={self.sku!r}, "
                f"description={self.description!r}, "
                f"price={self.price!r}, "
                f"stock={self.stock!r}, "
                f"category={self.category!r}, "
                f"created_at={self.created_at!r}, "
                f"updated_at={self.updated_at!r})")
