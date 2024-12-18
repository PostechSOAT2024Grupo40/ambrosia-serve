from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

from src.client.adapters.AuditMixin import AuditMixin


class Base(DeclarativeBase):
    pass


class CredentialTable(Base, AuditMixin):
    __tablename__ = "credentials"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    email: Mapped[str]
    password: Mapped[str]

    profile: Mapped["ProfileTable"] = relationship(back_populates="credential",
                                                   cascade="all, delete",
                                                   passive_deletes=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"CredentialTable(id={self.id}, "
                f"email={self.email}, "
                f"password={self.password}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at})")


class ProfileTable(Base, AuditMixin):
    __tablename__ = "profiles"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, autoincrement=False)
    first_name: Mapped[str]
    last_name: Mapped[str]
    cpf: Mapped[str]

    credential_id: Mapped[str] = mapped_column(ForeignKey("credentials.id", ondelete="CASCADE"))
    credential: Mapped["CredentialTable"] = relationship(back_populates="profile")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.cpf = kwargs.get('cpf')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    def __repr__(self):
        return (f"ProfileTable(id={self.id}, "
                f"first_name={self.first_name}, "
                f"last_name={self.last_name}, "
                f"cpf={self.cpf}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at})")
