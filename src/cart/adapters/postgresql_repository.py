import uuid
from typing import Any, Sequence, Optional

from sqlalchemy import select, delete, Row
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.cart.adapters.order_table import OrderTable, OrderProductTable, StatusTable, PaymentConditionTable
from src.cart.ports.repository_interface import IRepository

ORDER_COLS: tuple = (
    OrderTable.id,
    OrderTable.user_id,
    StatusTable.status,
    PaymentConditionTable.description.label('payment_condition'),
    OrderTable.created_at,
)


class PostgreSqlRepository(IRepository):

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all(self) -> Optional[Sequence[Row]]:
        stmt = (
            select(
                *ORDER_COLS
            )
            .join(StatusTable, OrderTable.status_id == StatusTable.id)
            .join(PaymentConditionTable, OrderTable.payment_condition_id == PaymentConditionTable.id)
            .order_by(OrderTable.status, OrderTable.created_at)
        )

        results = self.session.execute(stmt).all()

        if not results:
            return []

        return results

    def filter_by_id(self, order_id: str) -> Optional[Row]:
        stmt = (
            select(
                *ORDER_COLS
            )
            .join(StatusTable, OrderTable.status_id == StatusTable.id)
            .join(PaymentConditionTable, OrderTable.payment_condition_id == PaymentConditionTable.id)
            .order_by(OrderTable.status, OrderTable.created_at)
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

        status = self.create_or_get_status(values)
        payment_condition = self.create_or_get_payment_condition(values)

        order_data["status_id"] = status.id
        order_data["payment_condition_id"] = payment_condition.id

        del order_data["status"]
        del order_data["payment_condition"]
        stmt = insert(OrderTable).values(order_data)
        stmt = stmt.on_conflict_do_update(
            index_elements=[OrderTable.id],
            set_={key: order_data[key] for key in order_data if key != "id"}
        )
        self.session.execute(stmt)

    def create_or_get_payment_condition(self, values):
        payment_condition = (self.session.query(PaymentConditionTable)
                             .filter_by(description=values["payment_condition"]).first())
        if not payment_condition:
            payment_condition = PaymentConditionTable(id=str(uuid.uuid4()), description=values["payment_condition"])
            self.session.add(payment_condition)
            self.session.commit()
        return payment_condition

    def create_or_get_status(self, values):
        status = self.session.query(StatusTable).filter_by(status=values["status"]).first()
        if not status:
            status = StatusTable(id=str(uuid.uuid4()), status=values["status"])
            self.session.add(status)
            self.session.commit()
        return status

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

        self.session.commit()

    def delete(self, order_id: str):
        stmt = delete(OrderTable).where(OrderTable.id == order_id)
        self.session.execute(stmt)
