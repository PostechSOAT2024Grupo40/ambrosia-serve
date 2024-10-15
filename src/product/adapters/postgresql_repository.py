from typing import Dict, Any, List, Sequence

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.product.adapters.product_table import ProductTable
from src.product.ports.repository_interface import IProductRepository


class PostgreSqlProductRepository(IProductRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all(self) -> List[Dict]:
        stmt = select(ProductTable)
        results: Sequence[Row[tuple[ProductTable]]] = self.session.execute(stmt).all()
        if not results:
            return []

        return [row.to_dict() for row in results]

    def filter_by_sku(self, sku: str) -> Dict:
        stmt = select(ProductTable).where(ProductTable.sku == sku)
        result = self.session.execute(stmt).first()
        if not result:
            return {}

        return result[0].to_dict()

    def insert_update(self, values: Dict[str, Any]):
        stmt = insert(ProductTable).values(**values)
        stmt = stmt.on_conflict_do_update(
            index_elements=[ProductTable.id],
            set_=values
        )
        self.session.execute(stmt)

    def delete(self, sku: str):
        stmt = delete(ProductTable).where(ProductTable.sku == sku)
        self.session.execute(stmt)
