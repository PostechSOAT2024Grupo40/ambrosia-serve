import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_db_url():
    dbname = os.environ['POSTGRES_DB']
    user = os.environ['POSTGRES_USER']
    host = os.environ['POSTGRES_HOST']
    port = os.getenv('POSTGRES_PORT', 5432)
    password = os.environ['POSTGRES_PASSWORD']

    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")


def postgresql_session_factory() -> sessionmaker[Session]:
    return sessionmaker(bind=get_db_url(), autocommit=False)
