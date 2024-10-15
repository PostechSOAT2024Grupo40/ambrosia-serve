from sqlalchemy import Integer, Column, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.functions import now

Base = declarative_base()


class ProductTable(Base):
    __tablename__ = "products"

    id = Column(String(255), primary_key=True, nullable=False, autoincrement=False)
    sku = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=now())
    updated_at = Column(DateTime, nullable=False, default=now(), onupdate=now())

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
