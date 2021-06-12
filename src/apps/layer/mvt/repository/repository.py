#!-*-coding:utf-8-*-
from src.apps.layer.mvt.operations.envelope import Envelope
from src.db.async_connection import ASYNC_DB
from src.apps.layer.mvt.repository.envelope_sql import EnvelopeSQL
from typing import Generator
from sqlalchemy.sql.expression import text


class LayerMVTRepository:

    _env: EnvelopeSQL

    def __init__(self, layer_id: str, envelope: Envelope):
        self._env = EnvelopeSQL(layer_id, envelope)

    async def get_one(self) -> Generator[bytes, None, None]:
        pbf = None
        data = None

        async with ASYNC_DB.engine().begin() as conn:
            data = await conn.execute(text(self._env.sql()))
            pbf = data.fetchone()[0]

        if pbf is None:
            return b''

        return pbf
