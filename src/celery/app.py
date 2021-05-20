#!-*-coding:utf-8-*-

from celery import Celery
from src.config import ENVS


celery_app = Celery(
    'test_celery',
    broker=f'amqp://{ENVS.RABBIT_USER}:{ENVS.RABBIT_PASSWORD}@{ENVS.RABBIT_HOST}:{ENVS.RABBIT_PORT}//',
    backend='rpc://', # Url do backend dos resultado - valor rpc = enviar resultados de volta com mensgens AMPQ
    include=['src.apps.layer.upload.task']
)
