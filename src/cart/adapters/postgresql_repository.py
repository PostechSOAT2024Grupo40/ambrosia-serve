from typing import Any, Sequence, Optional

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

    def insert_update(self, values: dict[str, Any]):
        """Realiza insert ou update (UPSERT) na tabela de pedidos e seus produtos."""
        self._upsert_order(values)
        self._upsert_order_products(values["id"], values.get("products", []))

    def _upsert_order(self, values: dict[str, Any]):
        """Inserção ou atualização de um pedido."""
        order_data = {key: values[key] for key in values if key != "products"}

        stmt = insert(OrderTable).values(order_data)
        stmt = stmt.on_conflict_do_update(
            index_elements=[OrderTable.id],
            set_={key: order_data[key] for key in order_data if key != "id"}
        )
        self.session.execute(stmt)

    def _upsert_order_products(self, order_id: str, products: list[dict[str, Any]]):
        """Inserção ou atualização dos produtos relacionados a um pedido."""
        for product in products:
            product_data = product.copy()
            product_data["order_id"] = order_id

            stmt = insert(OrderProductTable).values(product_data)
            stmt = stmt.on_conflict_do_update(
                index_elements=[OrderProductTable.id],
                set_={key: product_data[key] for key in product_data if key != "id"}
            )
            self.session.execute(stmt)

    def delete(self, order_id: str):
        stmt = delete(OrderTable).where(OrderTable.id == order_id)
        self.session.execute(stmt)
