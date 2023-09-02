from tests.utils import (
    fake_int_id,
    fake_name,
    fake_email,
    fake_phone,
    fake_datetime,
)

INSERT_USERS_QUERY = """
    insert into users
    (
        id,
        name,
        email,
        phone,
        created,
        modified
    )
    VALUES
"""

BATCH_SIZE = 1010
COUNT_USERS_QUERY = "select count(1) from users final"


def get_random_user(user_id: int = None) -> dict:
    if not user_id:
        user_id = fake_int_id()
    name = fake_name()
    return {
        "id": user_id,
        "name": name,
        "email": fake_email(name),
        "phone": fake_phone(),
        "created": fake_datetime(),
        "modified": fake_datetime(),
    }


def test_insert(clickhouse_client, clickhouse_migrations):
    assert clickhouse_client.healthcheck()

    user_batch = [get_random_user(i + 1) for i in range(BATCH_SIZE)]

    clickhouse_client.execute_query(INSERT_USERS_QUERY, user_batch)

    res = clickhouse_client.execute_query(COUNT_USERS_QUERY)

    assert res[0][0] == BATCH_SIZE
