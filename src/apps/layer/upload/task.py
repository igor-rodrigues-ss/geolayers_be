#!-*-coding:utf-8-*-


import celery
from src.apps.layer.upload.validations.geom_inside_brazil import GeomInsideBrazil
from src.celery.app import celery_app
from celery.utils.log import get_task_logger
from src.db.sync_connection import SYNC_DB
from src.apps.layer.upload.operations.shapefile import Shapefile
from src.apps.layer.upload.repository.layer_upload import LayerUploadRepository
from src.apps.layer.upload.repository.task_save_layer import TaskSaveLayer
from src.celery.worker_init.br_geom import BRGeom


logger = get_task_logger(__name__)


class Base(celery.Task):

    def __init__(self):
        self._br_geom = BRGeom().geom()

    def br_geom(self):
        return self._br_geom


@celery_app.task(base=Base)
def save_layer(lyr_name: str, path: str, color: str, fill: bool):
    shape = Shapefile(path)
    exc = None

    with SYNC_DB.engine().connect() as conn:
        lyr_upload_repository = LayerUploadRepository(
            conn, lyr_name, shape.features(), color, fill
        )
        task_save_layer_repo = TaskSaveLayer(
            conn, save_layer.request.id, lyr_name
        )
        try:
            logger.info('Registrando a task')
            task_save_layer_repo.register_task()
            logger.info('Fazendo validação do território nacional')
            GeomInsideBrazil(save_layer.br_geom(), shape).validate()
            logger.info('Salvando dados')
            lyr_upload_repository.save()
        except Exception as ex:
            task_save_layer_repo.register_error(ex)
            exc = ex  # Exception armazenada para que o context seja finalizado
        else:
            task_save_layer_repo.register_success()

    if exc is not None:  # Interrompendo a task
        raise exc