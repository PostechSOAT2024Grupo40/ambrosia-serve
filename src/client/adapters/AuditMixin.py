from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import now


class AuditMixin:
    created_at: Mapped[datetime] = mapped_column(default=now())
    updated_at: Mapped[datetime] = mapped_column(default=now(), onupdate=now())

    def __init__(self, created_at: datetime, updated_at: datetime):
        self.created_at = created_at
        self.updated_at = updated_at
