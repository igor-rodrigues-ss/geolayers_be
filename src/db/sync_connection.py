#!-*-coding:utf-8-*-


from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from src.config import ENVS
from src.db.iconnection import IConnection


class SyncConnection(IConnection):

    _engine: Engine = None

    def __init__(self, host: str, db_name: str, user: str, password: str, port: int):
        self._engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
        )

    def engine(self) -> Engine:
        return self._engine


SYNC_DB = SyncConnection(
    ENVS.DB_HOST,
    ENVS.DB_NAME,
    ENVS.DB_USER,
    ENVS.DB_PASSWORD,
    ENVS.DB_PORT
)
