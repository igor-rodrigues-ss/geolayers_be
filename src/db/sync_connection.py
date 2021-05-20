#!-*-coding:utf-8-*-


from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from src.config import ENVS


class SyncConnection:

    _engine: Engine = None

    def __init__(self, host: str, db_name: str, user: str, password: str, port: int):
        self._host = host
        self._db_name = db_name
        self._user = user
        self._password = password
        self._port = port

    def create_engine(self):
        self._engine = create_engine(
            f"postgresql+psycopg2://{self._user}:{self._password}@{self._host}:{self._port}/{self._db_name}"
        )

    def engine(self) -> Engine:
        return self._engine

    # async def close(self):
    #     if self._pool is not None:
    #         self._pool.close()
    #         await self._pool.wait_closed()


SYNC_DB = SyncConnection(
    ENVS.DB_HOST,
    ENVS.DB_NAME,
    ENVS.DB_USER,
    ENVS.DB_PASSWORD,
    ENVS.DB_PORT
)
SYNC_DB.create_engine()
