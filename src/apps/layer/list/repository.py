#!-*-coding:utf-8-*-

from src.db.default_connection import DB_DEFAULT
from src.models import t_layer, t_styles
from typing import List


class LayerListRepo:

    async def list_all(self) -> List[dict]:
        data = {}
        async with DB_DEFAULT.pool().acquire() as conn:
            stmt = t_layer.join(t_styles).select()
            async for row in conn.execute(stmt):
                data[row.id] = {
                    'nome': row.nome, 'color': row.color,
                    'fill':  row.fill, 'show': False
                }
        return data
