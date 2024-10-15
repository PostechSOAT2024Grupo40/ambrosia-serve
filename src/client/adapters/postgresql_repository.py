from typing import Dict, List, Sequence

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.client.adapters.client_table import ClientTable
from src.client.ports.repository_interface import IClientRepository


class PostgreSqlClientRepository(IClientRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_users(self) -> List[Dict]:
        stmt = select(ClientTable)
        results: Sequence[Row[tuple[ClientTable]]] = self.session.execute(stmt).all()
        if not results:
            return []

        return [row[0].to_dict() for row in results]

    def get_user_by_cpf(self, cpf: str) -> Dict:
        stmt = select(ClientTable).where(ClientTable.cpf == cpf)
        results: Sequence[Row[tuple[ClientTable]]] = self.session.execute(stmt).first()
        if not results:
            return {}

        return results[0].to_dict()

    def get_user_by_email(self, email: str) -> Dict:
        stmt = select(ClientTable).where(ClientTable.email == email)
        results: Sequence[Row[tuple[ClientTable]]] = self.session.execute(stmt).first()
        if not results:
            return {}

        return results[0].to_dict()

    def create_user(self, user: Dict):
        stmt = insert(ClientTable).values(**user)
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

    def get_user_by_id(self, user_id: int) -> Dict:
        stmt = select(ClientTable).where(ClientTable.id == user_id)
        results: Sequence[Row[tuple[ClientTable]]] = self.session.execute(stmt).first()
        if not results:
            return {}

        return results[0].to_dict()
