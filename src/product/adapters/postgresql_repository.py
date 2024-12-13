from typing import Dict, Any, Sequence, Optional

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.product.adapters.product_table import ProductTable
from src.product.ports.repository_interface import IProductRepository


class PostgreSqlProductRepository(IProductRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all(self) -> Sequence[Row]:
        stmt = select(ProductTable)
        results = self.session.execute(stmt).all()
        if not results:
            return []

        return results

    def find_by_name(self, name: str) -> Optional[Row]:
        stmt = select(ProductTable).where(ProductTable.name == name)
        result = self.session.execute(stmt).first()
        if not result:
            return
        return result[0]

    def filter_by_id(self, product_id: str) -> Optional[Row]:
        stmt = select(ProductTable).where(ProductTable.id == product_id)

        result = self.session.execute(stmt).first()
        if not result:
            return

        return result[0]

    def insert_update(self, values: Dict[str, Any]):
        stmt = insert(ProductTable).values(**values)
        stmt = stmt.on_conflict_do_update(
            index_elements=[ProductTable.id],
            set_={key: values[key] for key in values if key != 'id'},
        )
        self.session.execute(stmt)

    def delete(self, product_id: str):
        stmt = delete(ProductTable).where(ProductTable.id == product_id)

        self.session.execute(stmt)
