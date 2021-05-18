#!-*-coding:utf-8-*-


from src.models import t_save_layer
from src.db.default_connection import DB_DEFAULT


class TasksSaveLayerRepository:

    async def list_all(self):
        async with DB_DEFAULT.pool().acquire() as conn:
            data = await conn.execute(t_save_layer.select())
            data = await data.fetchall()
            return data
