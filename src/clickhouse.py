import logging
import typing as t
from dataclasses import dataclass

from clickhouse_driver import Client

_logger = logging.getLogger(__name__)

HEALTHCHECK_QUERY = "SELECT 1"

FetchParams = t.Optional[dict]
InsertParams = t.List[dict]
QueryParams = t.Union[FetchParams, InsertParams]


@dataclass
class ClickHouseConfig:
    host: str = "localhost"
    port: int = 9000
    user: str = "default"
    password: str = ""
    database: str = ""


class ClickHouseClient:
    """
    An example ClickHouse client implementation
    """

    def __init__(self, config: ClickHouseConfig = None):
        if not config:
            # use default config if no config provided
            config = ClickHouseConfig()

        self.client = Client(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.database,
        )

    def execute_query(self, stmt, params: QueryParams = None) -> t.List[t.Tuple]:
        try:
            res = self.client.execute(stmt, params)
            return res
        except Exception:
            _logger.exception("ClickHouse query exception")
            raise

    def fetch_all(self, stmt, params: FetchParams = None) -> t.List[t.Tuple]:
        return self.execute_query(stmt, params)

    def insert_batch(self, stmt, data: InsertParams):
        return self.execute_query(stmt, data)

    def healthcheck(self) -> bool:
        try:
            res = self.execute_query(HEALTHCHECK_QUERY)
            if not res:
                return False
            if res[0][0] != 1:
                return False
        except Exception:
            return False
        else:
            return True
