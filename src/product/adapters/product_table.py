from typing import Any, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

from src.product.adapters.AuditMixin import AuditMixin


class Base(DeclarativeBase):
    pass


class CategoryTable(Base, AuditMixin):
    __tablename__ = "categories"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    category: Mapped[str] = mapped_column(nullable=False, unique=True)

    product: Mapped[list["ProductTable"]] = relationship(back_populates="category",
                                                         cascade="all, delete",
                                                         passive_deletes=True)

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.category = kwargs.get('category')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"CategoryTable(id={self.id!r}, "
                f"category={self.category!r}, "
                f"created_at={self.created_at!r}, "
                f"updated_at={self.updated_at!r})")


class ProductTable(Base, AuditMixin):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str]
    price: Mapped[float]
    stock: Mapped[int]
    image: Mapped[Optional[str]]

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))
    category: Mapped["CategoryTable"] = relationship(back_populates="product")

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.price = kwargs.get('price')
        self.stock = kwargs.get('stock')
        self.category = kwargs.get('category')
        self.image = kwargs.get('image')
        self.category_id = kwargs.get('category_id')
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
                f"category_id={self.category_id!r}, "
                f"created_at={self.created_at!r}, "
                f"updated_at={self.updated_at!r})")
