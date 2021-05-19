#!-*-coding:utf-8-*-

from aiopg.sa.engine import Engine
from aiopg.sa import create_engine
from src.db.managed_pool import managed_pool

from src.config import ENVS


class Database:

    _pool: Engine = None

    def __init__(self, host: str, db_name: str, user: str, password: str, port: int):
        self._host = host
        self._db_name = db_name
        self._user = user
        self._password = password
        self._port = port

    async def connect(self):
        self._pool = await create_engine(
            user=self._user,
            database=self._db_name,
            host=self._host,
            password=self._password,
            port=self._port,
            maxsize=10
        )

    def pool(self) -> Engine:
        return self._pool
        # return managed_pool(
        #     self._pool, db_name=self._db_name,
        #     max_attempt=10
        # )

    async def close(self):
        if self._pool is not None:
            self._pool.close()
            await self._pool.wait_closed()


DB_DEFAULT = Database(
    ENVS.DB_HOST,
    ENVS.DB_NAME,
    ENVS.DB_USER,
    ENVS.DB_PASSWORD,
    ENVS.DB_PORT
)
