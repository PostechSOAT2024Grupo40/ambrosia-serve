from sqlalchemy.orm import Session

from src.product.adapters.postgresql_repository import PostgreSqlProductRepository
from src.product.ports.unit_of_work_interface import IProductUnitOfWork


class ProductPostgreSqlUow(IProductUnitOfWork):

    def __init__(self, session_factory):
        self.session_factory = session_factory()


    def __enter__(self):
        self.session: Session = self.session_factory
        self.repository = PostgreSqlProductRepository(session=self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
