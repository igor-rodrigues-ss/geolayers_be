#!-*-coding:utf-8-*-

from src.db.async_connection import ASYNC_DB
from src.db.models import t_layer, t_styles
from typing import List


class LayerListRepository:

    async def list_all(self) -> List[dict]:
        data = {}
        async with ASYNC_DB.engine().begin() as conn:
            stmt = t_layer.join(t_styles).select()
            cur_res = await conn.execute(stmt)
            for row in cur_res:
                data[row.id] = {
                    'nome': row.nome, 'color': row.color,
                    'fill':  row.fill, 'show': False
                }
        return data
