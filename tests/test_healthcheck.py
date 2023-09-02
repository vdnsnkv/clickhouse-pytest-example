def test_healthcheck(clickhouse_client):
    assert clickhouse_client.healthcheck()
