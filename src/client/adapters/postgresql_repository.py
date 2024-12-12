from typing import Dict, Sequence, Optional

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.client.adapters.client_table import ClientTable

CLIENT_TABLE_COLUMNS = (ClientTable.id,
                        ClientTable.first_name,
                        ClientTable.last_name,
                        ClientTable.cpf,
                        ClientTable.email,
                        ClientTable.password)
from src.client.ports.repository_interface import IClientRepository


class PostgreSqlClientRepository(IClientRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_users(self) -> Optional[Sequence[Row[tuple]]]:
        stmt = select(*CLIENT_TABLE_COLUMNS)
        results = self.session.execute(stmt).all()
        if not results:
            return []

        return results

    def get_user_by_cpf(self, cpf: str) -> Optional[Row]:
        stmt = select(*CLIENT_TABLE_COLUMNS).where(ClientTable.cpf == cpf)
        results: Sequence[Row[tuple[ClientTable]]] = self.session.execute(stmt).first()
        if not results:
            return

        return results[0]

    def get_user_by_email(self, email: str) -> Optional[Row]:
        stmt = select(*CLIENT_TABLE_COLUMNS).where(ClientTable.email == email)
        results = self.session.execute(stmt).first()
        if not results:
            return

        return results[0]

    def create_user(self, user: Dict):
        stmt = insert(*CLIENT_TABLE_COLUMNS).values(**user)
        self.session.execute(stmt)

    def update_user(self, user: Dict):
        stmt = insert(ClientTable).values(**user)
        stmt = stmt.on_conflict_do_update(
            index_elements=[ClientTable.id],
            set_={key: user[key] for key in user if key != 'id'}
        )
        self.session.execute(stmt)

    def delete_user(self, user_id: int):
        stmt = delete(ClientTable).where(ClientTable.id == user_id)
        self.session.execute(stmt)

    def get_user_by_id(self, user_id: int) -> Optional[Row]:
        stmt = select(*CLIENT_TABLE_COLUMNS).where(ClientTable.id == user_id)
        results = self.session.execute(stmt).first()
        if not results:
            return

        return results[0]
