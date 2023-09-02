import pytest

from src.clickhouse import ClickHouseClient, ClickHouseConfig

TEST_DB = "test_database"
CREATE_DB_QUERY = f"create database if not exists {TEST_DB};"

DROP_TABLE_QUERIES = [
    f"drop table if exists {TEST_DB}.users;",
]

MIGRATION_FILES = [
    "migrations/0001_create_users_table.sql",
]


@pytest.fixture(scope="session")
def clickhouse_client():
    client = ClickHouseClient()
    client.execute_query(CREATE_DB_QUERY)

    client = ClickHouseClient(ClickHouseConfig(database=TEST_DB))

    for drop_table in DROP_TABLE_QUERIES:
        client.execute_query(drop_table)

    return client


@pytest.fixture(scope="session")
def clickhouse_migrations(clickhouse_client):
    migrations = []
    for fn in MIGRATION_FILES:
        with open(fn, "r") as f:
            migrations.append(f.read())

    for m in migrations:
        clickhouse_client.execute_query(m)
    return
