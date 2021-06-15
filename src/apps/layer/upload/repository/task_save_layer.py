#!-*-coding:utf-8-*-

from uuid import UUID
from src.db.models import t_save_layer
from sqlalchemy.engine.base import Connection
from src.config import (
    WORKER_STATUS_PENDING, WORKER_STATUS_SUCCESS, WORKER_STATUS_FAILURE
)


class TaskSaveLayer:

    _task_id: UUID
    _lyr_name: str
    _conn: Connection

    def __init__(
        self, conn: Connection, task_id: UUID, lyr_name: str
    ):
        self._conn = conn
        self._task_id = task_id
        self._lyr_name = lyr_name

    def register_task(self):
        self._conn.execute(
            t_save_layer.insert().values(
                id=self._task_id, status=WORKER_STATUS_PENDING, layer_name=self._lyr_name
            )
        )

    def register_error(self, exc: Exception):
        exc_cls = exc.__class__.__name__
        msg = f'{exc_cls}: {str(exc)}'
        self._conn.execute(
            t_save_layer.update().values(status=WORKER_STATUS_FAILURE, detail=msg).where(
                t_save_layer.c.id == self._task_id
            )
        )

    def register_success(self):
        self._conn.execute(
            t_save_layer.update().values(status=WORKER_STATUS_SUCCESS, detail='').where(
                t_save_layer.c.id == self._task_id
            )
        )