#!-*-coding:utf-8-*-


from src.config import ENVS, DB_POOL_MAX_SIZE
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.db.iconnection import IConnection
from sqlalchemy.sql.expression import text


class AsyncConnection(IConnection):

    _engine: AsyncEngine

    def __init__(self, host: str, db_name: str, user: str, password: str, port: int):
        self._engine = create_async_engine(
            f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}",
            pool_size=DB_POOL_MAX_SIZE,
        )

    def engine(self) -> AsyncEngine:
        return self._engine

    async def test_connection(self):
        async with ASYNC_DB.engine().connect() as conn:
            rcur = await conn.execute(text('SELECT 1'))
            return bool(rcur.fetchone()[0])


ASYNC_DB = AsyncConnection(
    ENVS.DB_HOST,
    ENVS.DB_NAME,
    ENVS.DB_USER,
    ENVS.DB_PASSWORD,
    ENVS.DB_PORT
)
