from typing import Dict, Any, Sequence, Optional

from sqlalchemy import select, delete, Row
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.cart.adapters.order_table import OrderTable, OrderProductTable
from src.cart.ports.repository_interface import IRepository


class PostgreSqlRepository(IRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all(self) -> Optional[Sequence[Row]]:
        stmt = (
            select(
                OrderTable.id.label('order_id'),
                OrderTable.user_id,
                OrderTable.status,
                OrderTable.payment_condition,
                OrderTable.created_at
            )
            .order_by(OrderTable.status, OrderTable.created_at)
        )

        results = self.session.execute(stmt).all()

        if not results:
            return []

        return results

    def filter_by_id(self, order_id: str) -> Optional[Row]:
        stmt = (
            select(
                OrderTable.id,
                OrderTable.user_id,
                OrderTable.status,
                OrderTable.payment_condition,
                OrderTable.created_at,
                OrderTable.updated_at
            )
            .where(OrderTable.id == order_id)
        )

        results = self.session.execute(stmt).all()

        if not results:
            return

        return results[0]

    def get_order_products(self, order_id: str) -> Sequence[Row]:
        stmt = select(OrderProductTable.id,
                      OrderProductTable.product_id,
                      OrderProductTable.quantity,
                      OrderProductTable.observation).where(OrderProductTable.order_id == order_id)
        results = self.session.execute(stmt).all()

        return results

    def insert_update(self, values: Dict[str, Any]):
        stmt_order = insert(OrderTable).values({key: values[key] for key in values if key != 'products'})
        stmt_order = stmt_order.on_conflict_do_update(
            index_elements=[OrderTable.id],
            set_={key: values[key] for key in values if key != 'id' and key != 'products'}
        )
        self.session.execute(stmt_order)

        for product in values['products']:
            product['order_id'] = values['id']
            stmt_product = insert(OrderProductTable).values(product)
            stmt_product = stmt_product.on_conflict_do_update(
                index_elements=[OrderProductTable.id],
                set_={key: product[key] for key in product if key != 'id'}
            )
            self.session.execute(stmt_product)

    def delete(self, sku: str):
        stmt = delete(OrderTable).where(OrderTable.id == sku)
        self.session.execute(stmt)
