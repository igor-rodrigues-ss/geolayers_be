#!-*-coding:utf-8-*-


from src.db.models import t_save_layer
from src.db.async_connection import ASYNC_DB


class TasksSaveLayerRepository:

    async def list_all(self):
        async with ASYNC_DB.engine().begin() as conn:
            data = await conn.execute(t_save_layer.select())
            return data.fetchall()
