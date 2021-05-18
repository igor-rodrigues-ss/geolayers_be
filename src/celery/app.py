#!-*-coding:utf-8-*-

from celery import Celery


celery_app = Celery(
    'test_celery',
    broker='amqp://guest:guest@localhost//',
    backend='rpc://', # Url do backend dos resultado - valor rpc = enviar resultados de volta com mensgens AMPQ
    include=['src.apps.layer.upload.task']
)
