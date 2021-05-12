#!-*-coding:utf-8-*-



from src.db.default_connection import DB_DEFAULT
from src.apps.layer.mvt.envelope_sql import EnvelopeSQL
from typing import Generator


class TileRepository:

    _env: EnvelopeSQL

    def __init__(self, env: EnvelopeSQL):
        self._env = env

    async def get_one(self) -> Generator[bytes, None, None]:
        pbf = None
        data = None

        async with DB_DEFAULT.pool().acquire() as conn:
        # async with DB_DEFAULT.pool() as conn:
            data = await conn.execute(self._env.sql())
            data = await data.fetchone()
            pbf = data[0]

        if pbf is None:
            return b''
        return pbf.tobytes()
