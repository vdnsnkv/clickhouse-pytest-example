# clickhouse-pytest-example

Repository with example setup for running ClickHouse integration tests with pytest.

### Setup environment

Create virtualenv and install requirements

```shell
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then start ClickHouse server

```shell
docker-compose -f ./docker-compose.yml up -d --remove-orphans
```

### Run tests

To run tests, use this command

```shell
pytest .
```