#!-*-coding:utf-8-*-

from src.db.async_connection import ASYNC_DB
from src.apps.layer.mvt.envelope_sql import EnvelopeSQL
from typing import Generator
from sqlalchemy.sql.expression import text


class LayerMVTRepository:

    _env: EnvelopeSQL

    def __init__(self, env: EnvelopeSQL):
        self._env = env

    async def get_one(self) -> Generator[bytes, None, None]:
        pbf = None
        data = None

        async with ASYNC_DB.engine().begin() as conn:
            data = await conn.execute(text(self._env.sql()))
            pbf = data.fetchone()[0]

        if pbf is None:
            return b''

        return pbf
