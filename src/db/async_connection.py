#!-*-coding:utf-8-*-


from src.config import ENVS, DB_POOL_MAX_SIZE
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine


class AsyncConnection:

    _engine: AsyncEngine = None

    def __init__(self, host: str, db_name: str, user: str, password: str, port: int):
        self._host = host
        self._db_name = db_name
        self._user = user
        self._password = password
        self._port = port

    def create_engine(self):
        self._engine = create_async_engine(
            f"postgresql+asyncpg://{self._user}:{self._password}@{self._host}:{self._port}/{self._db_name}",
            pool_size=DB_POOL_MAX_SIZE,
        )

    def engine(self) -> AsyncEngine:
        return self._engine

    # async def close(self):
    #     if self._pool is not None:
    #         self._pool.close()
    #         await self._pool.wait_closed()


ASYNC_DB = AsyncConnection(
    ENVS.DB_HOST,
    ENVS.DB_NAME,
    ENVS.DB_USER,
    ENVS.DB_PASSWORD,
    ENVS.DB_PORT
)
ASYNC_DB.create_engine()
