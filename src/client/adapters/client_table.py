from datetime import datetime

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
    created_at: Mapped[datetime] = mapped_column(default=now())
    updated_at: Mapped[datetime] = mapped_column(default=now(), onupdate=now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.cpf = kwargs.get('cpf')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"ClientTable(id={self.id}, "
                f"first_name={self.first_name}, "
                f"last_name={self.last_name}, "
                f"cpf={self.cpf}, "
                f"email={self.email}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at})")
