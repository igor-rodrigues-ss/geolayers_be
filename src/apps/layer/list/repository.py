#!-*-coding:utf-8-*-

from src.db.default_connection import DB_DEFAULT
from src.models import t_layer
from typing import List


class LayerListRepo:

    async def list_all(self) -> List[dict]:
        data = {}
        async with DB_DEFAULT.pool().acquire() as conn:
            async for row in conn.execute(t_layer.select()):
                data[row.id] = {'nome': row.nome, 'show': False}
        return data
