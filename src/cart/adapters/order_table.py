from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.functions import now

Base = declarative_base()


class OrderTable(Base):
    __tablename__ = "orders"

    id = Column(String(255), primary_key=True, nullable=False, autoincrement=False)
    user_id = Column(String(255), nullable=False)
    status = Column(Integer, nullable=False)
    payment_condition = Column(Integer, nullable=False)
    products = relationship("OrderProductTable", back_populates="order")
    created_at = Column(DateTime, nullable=False, default=now())
    updated_at = Column(DateTime, nullable=False, default=now(), onupdate=now())

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class OrderProductTable(Base):
    __tablename__ = "order_products"

    id = Column(String(255), primary_key=True, nullable=False, autoincrement=False)
    product_id = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    observation = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=now())
    updated_at = Column(DateTime, nullable=False, default=now(), onupdate=now())

    order_id = Column(String(255), ForeignKey("orders.id"), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
