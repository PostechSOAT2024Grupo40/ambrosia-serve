import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from cart.adapters.order_table import Base as OrderBase
from client.adapters.client_table import Base as ClientBase
from product.adapters.product_table import Base as ProductBase


def postgresql_session_factory() -> sessionmaker[Session]:
    dbname = os.environ['POSTGRES_DB']
    user = os.environ['POSTGRES_USER']
    host = os.environ['POSTGRES_HOST']
    port = os.getenv('POSTGRES_PORT', 5432)
    password = os.environ['POSTGRES_PASSWORD']

    ENGINE = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

    try:

        all_bases = [ProductBase, ClientBase, OrderBase]
        for base in all_bases:
            base.metadata.create_all(ENGINE, checkfirst=True)
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

    return sessionmaker(bind=ENGINE, autocommit=False)
