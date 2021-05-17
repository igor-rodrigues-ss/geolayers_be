from src.apps.layer.upload.default.service import LayerUpload

from src.celery.app import celery_app
import os
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

from celery.signals import worker_process_init, worker_process_shutdown
from src.apps.layer.upload.celery.repository import LayerImportRepo
from src.apps.layer.upload.celery.shapefile import Shapefile



# @worker_process_init.connect
# def init_worker(**kwargs):
#     logger.info('Inicializando o worker.')
#
# @worker_process_shutdown.connect
# def shutdown_worker(**kwargs):
#     logger.info('Encerrando o worker')
#
import os

@celery_app.task
def save_layer(path, color, fill):

    def _layer_name(path):
        fname = os.path.basename(path)
        fname_splited = fname.split('.')
        return '.'.join(fname_splited[:-1])

    shape = Shapefile(path)
    repo = LayerImportRepo(_layer_name(path), shape.features(), color, fill)
    repo.save()