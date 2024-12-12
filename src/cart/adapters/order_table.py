from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.functions import now


class Base:
    pass


class OrderTable(Base):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False, index=True)
    user_id: Mapped[str]
    status: Mapped[int]
    payment_condition: Mapped[str]
    products: Mapped["OrderProductTable"] = relationship("OrderProductTable", back_populates="order")
    created_at: Mapped[DateTime] = mapped_column(default=now())
    updated_at: Mapped[DateTime] = mapped_column(default=now(), onupdate=now())


class OrderProductTable(Base):
    __tablename__ = "order_products"

    id: Mapped[str] = mapped_column(String(255), primary_key=True, nullable=False, autoincrement=False)
    product_id: Mapped[str]
    quantity: Mapped[int]
    observation: Mapped[str]
    created_at: Mapped[DateTime] = mapped_column(default=now())
    updated_at: Mapped[DateTime] = mapped_column(default=now(), onupdate=now())

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"))
    order = relationship("OrderTable", back_populates="products")

