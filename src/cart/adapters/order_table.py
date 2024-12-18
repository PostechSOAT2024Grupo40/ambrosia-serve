from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

from src.cart.adapters.AuditMixin import AuditMixin


class Base(DeclarativeBase):
    pass


class StatusTable(Base, AuditMixin):
    __tablename__ = "status"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    status: Mapped[str] = mapped_column(nullable=False, unique=True)

    orders: Mapped[list["OrderTable"]] = relationship(back_populates="status",
                                                      cascade="all, delete",
                                                      passive_deletes=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.status = kwargs.get('status')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"StatusTable(id={self.id}, "
                f"status={self.status}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at})")


class PaymentConditionTable(Base, AuditMixin):
    __tablename__ = "payment_conditions"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    description: Mapped[str]

    order: Mapped["OrderTable"] = relationship(back_populates="payment_condition",
                                               cascade="all, delete",
                                               passive_deletes=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.description = kwargs.get('description')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"PaymentConditionTable(id={self.id}, "
                f"description={self.description}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at})")


class OrderTable(Base, AuditMixin):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False, index=True)
    user_id: Mapped[str]
    status_id: Mapped[str] = mapped_column(ForeignKey("status.id", ondelete="CASCADE"))
    status: Mapped["StatusTable"] = relationship(back_populates="orders")
    payment_condition_id: Mapped[str] = mapped_column(ForeignKey("payment_conditions.id", ondelete="CASCADE"))
    payment_condition: Mapped["PaymentConditionTable"] = relationship(back_populates="order")
    total: Mapped[float]
    products: Mapped[list["OrderProductTable"]] = relationship(back_populates="order",
                                                               cascade="all, delete",
                                                               passive_deletes=True)

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


class OrderProductTable(Base, AuditMixin):
    __tablename__ = "order_products"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    product_id: Mapped[str]
    quantity: Mapped[int]
    observation: Mapped[str]

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"))
    order: Mapped["OrderTable"] = relationship(back_populates="products")

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
