#!-*-coding:utf-8-*-


import os
from pydantic import BaseSettings


ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CACHE_EXPTIME = 0

CACHE_POOL_SIZE_MIN = 4
CACHE_POOL_SIZE_MAX = 30
MVT_ALLOWED_FORMATS = ['pbf', 'mvt']

LOG_PATH = '/tmp/geolayers.log'
FORMAT_LOG = """<green>{time:DD-MM-YYYY HH:mm:ss}</green> | <level>{level}</level> | <level>{name}:{function}</level> | <level>{message}</level>"""

MERCATOR_SRID = 3857
MVT_DENSIFY_FACTOR = 4


WORKER_STATUS_PENDING = 'PENDING'
WORKER_STATUS_SUCCESS = 'SUCCESS'
WORKER_STATUS_FAILURE = 'FAILURE'


class Envs(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: str = '5432'
    DB_NAME: str = 'geolayer'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = '123456'
    CACHE_HOST: str = 'localhost'
    CACHE_PORT: str = '11211'
    RABBIT_HOST: str = 'localhost'
    RABBIT_USER: str = 'guest'
    RABBIT_PASSWORD: str = 'guest'
    RABBIT_PORT: str = '5672'



ENVS = Envs()


