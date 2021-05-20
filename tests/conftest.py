#!-*-coding:utf-8-*-

import os
import pytest
import testing.postgresql
from sqlalchemy import create_engine

from fastapi.testclient import TestClient


class Config:

    def __init__(self):
        self.PG = testing.postgresql.Postgresql()

    def create_test_database(self):
        engine = create_engine(self.PG.url())
        sql = os.environ['SQL_MIGRATIONS_PATH']

        os.environ['DB_NAME'] = self.PG.dsn()['database']
        os.environ['DB_PORT'] = str(self.PG.dsn()['port'])
        os.environ['DB_HOST'] = self.PG.dsn()['host']

        with engine.connect() as conn:
            with open(sql) as f:
                conn.execute(f.read())

    def drop_test_database(self):
        self.PG.stop()

    def app(self):
        from src.app import app
        return app

    def config_celery(self):
        from src.celery.app import celery_app
        celery_app.conf.update(CELERY_ALWAYS_EAGER=True)


config = Config()


def url_for(name: str, **args):
    return config.app().url_path_for(name, **args)


@pytest.fixture(scope='session')
def client():
    config.config_celery()
    with TestClient(config.app()) as tc:
        yield tc


def pytest_sessionstart(session):
    config.create_test_database()


def pytest_sessionfinish(session, exitstatus):
    config.drop_test_database()


#from async_asgi_testclient import TestClient
# async with TestClient(app) as client:
# await client.post(
# "/layer/upload",
# files={
#     "file": ("file", open(PATH, "rb"), 'multipart/form-data'),
#     'color': '#222', 'fill': 'true'
# }
