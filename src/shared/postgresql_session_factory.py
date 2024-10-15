import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def postgresql_session_factory() -> sessionmaker[Session]:
    dbname = os.environ['POSTGRES_DB']
    user = os.environ['POSTGRES_USER']
    host = os.environ['POSTGRES_HOST']
    port = os.getenv('POSTGRES_PORT', 5432)
    password = os.environ['POSTGRES_PASSWORD']

    ENGINE = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

    return sessionmaker(bind=ENGINE, autocommit=False)
