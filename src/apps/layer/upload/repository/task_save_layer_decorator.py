#!-*-coding:utf-8-*-

from uuid import UUID
from src.db.models import t_save_layer
from sqlalchemy.engine.base import Connection
from src.apps.layer.upload.repository.ilayer_upload import ILayerUploadRepository
from src.config import WORKER_STATUS_PENDING, WORKER_STATUS_SUCCESS, WORKER_STATUS_FAILURE


class TaskSaveLayer(ILayerUploadRepository):

    _repo: ILayerUploadRepository
    _task_id: UUID
    _lyr_name: str
    _conn: Connection

    def __init__(
        self, conn: Connection, task_id: UUID, lyr_name: str, repo: ILayerUploadRepository
    ):
        self._repo = repo
        self._conn = conn
        self._task_id = task_id
        self._lyr_name = lyr_name

    def _register_task(self):
        self._conn.execute(
            t_save_layer.insert().values(
                id=self._task_id, status=WORKER_STATUS_PENDING, layer_name=self._lyr_name
            )
        )

    def _register_error(self, exc: Exception):
        exc_cls = exc.__class__.__name__
        msg = f'{exc_cls}: {str(exc)}'
        self._conn.execute(
            t_save_layer.update().values(status=WORKER_STATUS_FAILURE, detail=msg).where(
                t_save_layer.c.id == self._task_id
            )
        )

    def _register_success(self):
        self._conn.execute(
            t_save_layer.update().values(status=WORKER_STATUS_SUCCESS, detail='').where(
                t_save_layer.c.id == self._task_id
            )
        )

    def save(self):
        try:
            self._register_task()
            self._repo.save()
        except Exception as exc:
            self._register_error(exc)
            raise exc
        else:
            self._register_success()
