import pytest
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="module")
def postgres_container():
    """Start a PostgreSQL container."""
    with PostgresContainer("postgres:15.2") as postgres:
        yield postgres


@pytest.fixture(scope="module")
def db_connection(postgres_container):
    """Set up a database connection and initialize schema."""
    conn = psycopg2.connect(
        dbname=postgres_container.get_database_name(),
        user=postgres_container.get_username(),
        password=postgres_container.get_password(),
        host=postgres_container.get_container_host_ip(),
        port=postgres_container.get_exposed_port(5432),
    )
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(open("products_schema.sql", "r").read())
    yield conn
    cursor.close()
    conn.close()
