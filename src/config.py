#!-*-coding:utf-8-*-


import os
from pydantic import BaseSettings


# Health Check
UP = 'UP'
DOWN = 'DOWN'

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FILE_MODELS_PATH = os.path.join(ROOT_DIR, 'static', 'file_models')

DB_POOL_MAX_SIZE = 4

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
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    CACHE_HOST: str
    CACHE_PORT: str
    RABBIT_HOST: str
    RABBIT_USER: str
    RABBIT_PASSWORD: str
    RABBIT_PORT: str
    RABBIT_VHOST: str
    STORAGE_PATH: str


ENVS = Envs()


UPLOADED_FILE_PATH = os.path.join(ENVS.STORAGE_PATH, 'uploaded_files')

# External Services Names
CELERY_SERVICE = 'Celery'
MEM_CACHED_SERVICE = 'MemCached'
NO_CACHE_SERVICE = 'NoCache'
DB_SERVICE = 'DB'

# First DB Connection
MAX_ATTEMPS = 10
SLEEP_FOR_NEXT_ATTEMPT = 3

# Tempo total = MAX_ATTEMPS x SLEEPT_FOR_NEXT_ATTEMPT

BASE_FILES = os.path.join(ROOT_DIR, 'static', 'base_files')
BR_GEOM_PATH = os.path.join(BASE_FILES, 'br_geom.wkt')