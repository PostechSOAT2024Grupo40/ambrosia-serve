from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    pass


class OrderTable(Base):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False, index=True)
    user_id: Mapped[str]
    status: Mapped[int]
    payment_condition: Mapped[str]
    total: Mapped[float]
    products: Mapped["OrderProductTable"] = relationship("OrderProductTable", back_populates="order")
    created_at: Mapped[datetime] = mapped_column(default=now())
    updated_at: Mapped[datetime] = mapped_column(default=now(), onupdate=now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.user_id = kwargs.get('user_id')
        self.status = kwargs.get('status')
        self.payment_condition = kwargs.get('payment_condition')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"OrderTable(id={self.id}, "
                f"user_id={self.user_id}, "
                f"status={self.status}, "
                f"payment_condition={self.payment_condition}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at})")


class OrderProductTable(Base):
    __tablename__ = "order_products"

    id: Mapped[str] = mapped_column(String(255), primary_key=True, nullable=False, autoincrement=False)
    product_id: Mapped[str]
    quantity: Mapped[int]
    observation: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=now())
    updated_at: Mapped[datetime] = mapped_column(default=now(), onupdate=now())

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"))
    order = relationship("OrderTable", back_populates="products")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.product_id = kwargs.get('product_id')
        self.quantity = kwargs.get('quantity')
        self.observation = kwargs.get('observation')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        self.order_id = kwargs.get('order_id')

    def __repr__(self):
        return (f"OrderProductTable(id={self.id}, "
                f"product_id={self.product_id}, "
                f"quantity={self.quantity}, "
                f"observation={self.observation}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at}, "
                f"order_id={self.order_id})")
