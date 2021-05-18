#!-*-coding:utf-8-*-

CACHE_EXPTIME = 0
CACHE_HOST = 'localhost'
CACHE_PORT = 11211
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
