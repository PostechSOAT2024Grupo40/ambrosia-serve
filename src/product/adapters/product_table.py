from datetime import datetime
from typing import Any, Optional

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    pass


class ProductTable(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str]
    price: Mapped[float]
    stock: Mapped[int]
    category: Mapped[str]
    image: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(default=now())
    updated_at: Mapped[datetime] = mapped_column(default=now(), onupdate=now())

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.price = kwargs.get('price')
        self.stock = kwargs.get('stock')
        self.category = kwargs.get('category')
        self.image = kwargs.get('image')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"ProductTable(id={self.id!r}, "
                f"name={self.name!r}, "
                f"description={self.description!r}, "
                f"price={self.price!r}, "
                f"stock={self.stock!r}, "
                f"category={self.category!r}, "
                f"image={self.image!r}, "
                f"created_at={self.created_at!r}, "
                f"updated_at={self.updated_at!r})")
