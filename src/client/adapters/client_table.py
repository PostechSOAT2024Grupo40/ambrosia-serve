from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.functions import now

Base = declarative_base()


class ClientTable(Base):
    __tablename__ = "clients"

    id = Column(String(255), primary_key=True, nullable=False, autoincrement=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    cpf = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=now())
    updated_at = Column(DateTime, nullable=False, default=now(), onupdate=now())

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
