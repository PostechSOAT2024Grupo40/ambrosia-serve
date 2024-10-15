from typing import Dict, List, Sequence, Any

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.cart.adapters.order_products_table import OrderProductTable
from src.cart.adapters.order_table import OrderTable
from src.cart.ports.repository_interface import IRepository


class PostgreSqlRepository(IRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all(self) -> List[Dict]:
        stmt = select(OrderTable).order_by(OrderTable.status, OrderTable.created_at)
        results: Sequence[Row[tuple[OrderTable]]] = self.session.execute(stmt).all()
        if not results:
            return []

        return [row.to_dict() for row in results]

    def filter_by_id(self, order_id: str) -> Dict:
        stmt = select(OrderTable).where(OrderTable.id == order_id)
        results: Sequence[Row[tuple[OrderTable]]] = self.session.execute(stmt).first()
        if not results:
            return {}

        return results[0].to_dict()

    def insert_update(self, values: Dict[str, Any]):
        stmt_product = insert(OrderProductTable).values(**values['products'])
        stmt_product = stmt_product.on_conflict_do_update(
            index_elements=[OrderProductTable.id],
            set_=values['products']
        )
        self.session.execute(stmt_product)

        stmt = insert(OrderTable).values(**values)
        stmt = stmt.on_conflict_do_update(
            index_elements=[OrderTable.id],
            set_=values
        )
        self.session.execute(stmt)

    def delete(self, sku: str):
        stmt = delete(OrderTable).where(OrderTable.id == sku)
        self.session.execute(stmt)
