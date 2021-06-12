#!-*-coding:utf-8-*-


from src.celery.app import celery_app
from celery.utils.log import get_task_logger
from src.db.sync_connection import SYNC_DB
from src.apps.layer.upload.operations.shapefile import Shapefile
from src.apps.layer.upload.repository.layer_upload import LayerUploadRepository
from src.apps.layer.upload.repository.task_save_layer_decorator import TaskSaveLayer


logger = get_task_logger(__name__)


@celery_app.task
def save_layer(lyr_name: str, path: str, color: str, fill: bool):
    shape = Shapefile(path)
    exc = None

    with SYNC_DB.engine().connect() as conn:
        try:
            repo = LayerUploadRepository(conn, lyr_name, shape.features(), color, fill)
            repo = TaskSaveLayer(conn, save_layer.request.id, lyr_name, repo)
            repo.save()
        except Exception as ex:
            exc = ex

    if exc is not None:
        raise exc