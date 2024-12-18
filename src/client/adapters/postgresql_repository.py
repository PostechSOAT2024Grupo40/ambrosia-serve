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
        credential = self.create_or_get_credential(user_id=user['id'], email=user['email'], password=user['password'])
        del user['email']
        del user['password']
        profile = ProfileTable(credential_id=credential.id, **user)
        self.session.add(profile)
        self.session.commit()

    def create_or_get_credential(self, user_id: str, email: str, password: str):
        credential = self.session.query(CredentialTable).join(CredentialTable.profile).filter(
            ProfileTable.id == user_id).first()
        if not credential:
            credential = CredentialTable(id=str(uuid.uuid4()), email=email, password=password)
            self.session.add(credential)
            self.session.commit()
        return credential

    def update_user(self, user: Dict):
        credential_data = self.create_or_get_credential(user_id=user['id'], email=user['email'],
                                                        password=user['password'])
        if credential_data:
            stmt = insert(CredentialTable).values(id=credential_data.id, email=user['email'], password=user['password'])
            stmt = stmt.on_conflict_do_update(
                index_elements=[CredentialTable.id],
                set_=dict(email=user['email'], password=user['password'])
            )
            self.session.execute(stmt)

        self.session.commit()

        profile_data = {key: user[key] for key in user if key not in ['email', 'password']}
        stmt = insert(ProfileTable).values(credential_id=credential_data.id, **profile_data)
        stmt = stmt.on_conflict_do_update(
            index_elements=[ProfileTable.id],
            set_=profile_data
        )
        self.session.execute(stmt)

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
