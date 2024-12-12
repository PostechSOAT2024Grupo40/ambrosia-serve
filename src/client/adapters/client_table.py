from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import now


class Base:
    pass


class ClientTable(Base):
    __tablename__ = "clients"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    first_name: Mapped[str]
    last_name: Mapped[str]
    cpf: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[DateTime] = mapped_column(default=now())
    updated_at: Mapped[DateTime] = mapped_column(default=now(), onupdate=now())
