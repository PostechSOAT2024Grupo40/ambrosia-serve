import uuid
from typing import Dict, Sequence, Optional

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.client.adapters.client_table import ProfileTable, CredentialTable
from src.client.ports.repository_interface import IClientRepository

PROFILE_COLS: tuple = (
    ProfileTable.id,
    ProfileTable.first_name,
    ProfileTable.last_name,
    ProfileTable.cpf,
    CredentialTable.email,
    CredentialTable.password,
)


class PostgreSqlClientRepository(IClientRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_users(self) -> Optional[Sequence[Row[tuple]]]:
        stmt = select(*PROFILE_COLS).join(ProfileTable.credential)
        results = self.session.execute(stmt).all()
        if not results:
            return []

        return results

    def get_user_by_cpf(self, cpf: str) -> Optional[Row]:
        stmt = select(*PROFILE_COLS).join(ProfileTable.credential).where(ProfileTable.cpf == cpf)
        results = self.session.execute(stmt).first()
        if not results:
            return

        return results

    def get_user_by_email(self, email: str) -> Optional[Row]:
        stmt = select(*PROFILE_COLS).join(ProfileTable.credential).where(CredentialTable.email == email)
        results = self.session.execute(stmt).first()
        if not results:
            return

        return results

    def create_user(self, user: Dict):
        credential = self.save_credential(email=user['email'], password=user['password'])

        profile = ProfileTable(credential_id=credential.id, **user)
        self.session.add(profile)
        self.session.commit()

    def save_credential(self, email: str, password: str):
        credential = CredentialTable(id=str(uuid.uuid4()), email=email, password=password)
        self.session.add(credential)
        self.session.commit()
        return credential

    def update_user(self, user: Dict):
        profile_data = {key: user[key] for key in user if key not in ['email', 'password']}
        stmt = insert(ProfileTable).values(**profile_data)
        stmt = stmt.on_conflict_do_update(
            index_elements=[ProfileTable.id],
            set_=profile_data
        )
        self.session.execute(stmt)

        credential_data = {key: user[key] for key in user if key in ['email', 'password']}
        if credential_data:
            stmt = insert(CredentialTable).values(id=user['credential_id'], **credential_data)
            stmt = stmt.on_conflict_do_update(
                index_elements=[CredentialTable.id],
                set_=credential_data
            )
            self.session.execute(stmt)

        self.session.commit()

    def delete_user(self, user_id: str):
        stmt = delete(ProfileTable).where(ProfileTable.id == user_id)
        self.session.execute(stmt)
        self.session.commit()

    def get_user_by_id(self, user_id: str) -> Optional[Row]:
        stmt = select(*PROFILE_COLS).join(ProfileTable.credential).where(ProfileTable.id == user_id)
        results = self.session.execute(stmt).first()
        if not results:
            return

        return results
