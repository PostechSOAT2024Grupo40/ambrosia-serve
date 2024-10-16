from typing import Dict, List, Any

from sqlalchemy import select, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from product.adapters.product_table import ProductTable
from src.cart.adapters.order_table import OrderTable, OrderProductTable
from src.cart.ports.repository_interface import IRepository


class PostgreSqlRepository(IRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all(self) -> List[Dict]:

        stmt = (
            select(
                OrderTable.id,
                OrderTable.user_id,
                OrderTable.status,
                OrderTable.payment_condition,
                OrderTable.created_at,
                OrderTable.updated_at,
                OrderProductTable.quantity,
                OrderProductTable.observation,
                ProductTable.sku,
                ProductTable.description,
                ProductTable.price,
                ProductTable.category,
                ProductTable.stock,
                ProductTable.id
            )
            .join(OrderProductTable, OrderTable.id == OrderProductTable.order_id)
            .join(ProductTable, ProductTable.sku == OrderProductTable.product_id)
            .order_by(OrderTable.status, OrderTable.created_at)
        )

        results = self.session.execute(stmt).all()

        if not results:
            return []

        # Processing the results into a more readable format
        response = []
        for row in results:
            order_data = {
                'id': row[0],
                'user_id': row[1],
                'status': row[2],
                'payment_condition': row[3],
                'created_at': row[4],
                'updated_at': row[5],
                'products': []
            }

            product_data = {
                'sku': row[8],
                'description': row[9],
                'price': row[10],
                'quantity': row[6],
                'observation': row[7],
                'category': row[11],
                'stock': row[12],
                'id': row[13]
            }
            order_data['products'].append(product_data)
            response.append(order_data)

        return response

    def filter_by_id(self, order_id: str) -> Dict:

        stmt = (
            select(
                OrderTable.id,
                OrderTable.user_id,
                OrderTable.status,
                OrderTable.payment_condition,
                OrderTable.created_at,
                OrderTable.updated_at,
                OrderProductTable.quantity,
                OrderProductTable.observation,
                ProductTable.sku,
                ProductTable.description,
                ProductTable.price,
                ProductTable.category,
                ProductTable.stock,
                ProductTable.id
            )
            .join(OrderProductTable, OrderTable.id == OrderProductTable.order_id)
            .join(ProductTable, ProductTable.sku == OrderProductTable.product_id)
            .where(OrderTable.id == order_id)
        )

        results = self.session.execute(stmt).all()

        if not results:
            return {}

        # Processing the single result
        order_data = {
            'id': results[0][0],
            'user_id': results[0][1],
            'status': results[0][2],
            'payment_condition': results[0][3],
            'created_at': results[0][4],
            'updated_at': results[0][5],
            'products': []
        }

        for row in results:
            product_data = {
                'sku': row[8],
                'description': row[9],
                'price': row[10],
                'quantity': row[6],
                'observation': row[7],
                'category': row[11],
                'stock': row[12],
                'id': row[13]
            }
            order_data['products'].append(product_data)

        return order_data

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
