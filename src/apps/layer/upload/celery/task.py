#!-*-coding:utf-8-*-


import os
from src.celery.app import celery_app
from celery.utils.log import get_task_logger
from src.apps.layer.upload.celery.repository import LayerImportRepo
from src.apps.layer.upload.celery.shapefile import Shapefile
from src.db.default_conn_celery import engine
from src.models import t_save_layer

logger = get_task_logger(__name__)

# @worker_process_init.connect
# def init_worker(**kwargs):
#     logger.info('Inicializando o worker.')
#
# @worker_process_shutdown.connect
# def shutdown_worker(**kwargs):
#     logger.info('Encerrando o worker')
#


@celery_app.task
def save_layer(lyr_name, path, color, fill):
    shape = Shapefile(path)
    repo = LayerImportRepo(lyr_name, shape.features(), color, fill)
    #repo = SaveLayerTaskRepo(LayerImportRepo(lyr_name, shape.features(), color, fill), task_id)
    repo.save(save_layer.request.id)