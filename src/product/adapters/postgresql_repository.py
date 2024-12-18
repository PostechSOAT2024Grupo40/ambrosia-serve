import uuid
from typing import Any, Sequence, Optional

from sqlalchemy import select, Row, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.product.adapters.product_table import ProductTable, CategoryTable
from src.product.ports.repository_interface import IProductRepository

PRODUCTS_COLS: tuple = (
    ProductTable.id,
    ProductTable.name,
    ProductTable.description,
    CategoryTable.category,
    ProductTable.image,
    ProductTable.price,
    ProductTable.stock,
)


class PostgreSqlProductRepository(IProductRepository):

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all(self) -> Sequence[Row]:
        stmt = select(*PRODUCTS_COLS).join(ProductTable.category)
        results = self.session.execute(stmt).all()
        if not results:
            return []

        return results

    def find_by_name(self, name: str) -> Optional[Row]:
        stmt = select(*PRODUCTS_COLS).join(ProductTable.category).where(ProductTable.name == name)
        result = self.session.execute(stmt).first()
        if not result:
            return
        return result

    def filter_by_id(self, product_id: str) -> Optional[Row]:
        stmt = select(*PRODUCTS_COLS).join(ProductTable.category).where(ProductTable.id == product_id)

        result = self.session.execute(stmt).first()
        if not result:
            return

        return result

    def insert_update(self, values: dict[str, Any]):
        category = self.create_or_get_category(values['category'])

        values['category_id'] = category.id
        del values['category']
        stmt = insert(ProductTable).values(**values)
        stmt = stmt.on_conflict_do_update(
            index_elements=[ProductTable.id],
            set_={key: values[key] for key in values if key != 'id'},
        )
        self.session.execute(stmt)
        self.session.commit()

    def create_or_get_category(self, category: str):
        _category = self.session.query(CategoryTable).filter_by(category=category).first()
        if not _category:
            _category = CategoryTable(
                id=str(uuid.uuid4()),
                category=category
            )
            self.session.add(_category)
            self.session.commit()
        return _category

    def delete(self, product_id: str):
        stmt = delete(ProductTable).where(ProductTable.id == product_id)

        self.session.execute(stmt)
        self.session.commit()
