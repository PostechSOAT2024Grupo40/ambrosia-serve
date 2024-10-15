from typing import Dict, List, Sequence, Any

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.cart.adapters.order_table import OrderTable, OrderProductTable
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
        stmt_order = insert(OrderTable).values({key: values[key] for key in values if key != 'products'})
        stmt_order = stmt_order.on_conflict_do_update(
            index_elements=[OrderTable.id],
            set_={key: values[key] for key in values if key != 'id' and key != 'products'}
        )
        self.session.execute(stmt_order)

        for product in values['products']:
            stmt_product = insert(OrderProductTable).values(product)
            stmt_product = stmt_product.on_conflict_do_update(
                index_elements=[OrderProductTable.id],
                set_={key: product[key] for key in product if key != 'id'}
            )
            self.session.execute(stmt_product)

    def delete(self, sku: str):
        stmt = delete(OrderTable).where(OrderTable.id == sku)
        self.session.execute(stmt)
