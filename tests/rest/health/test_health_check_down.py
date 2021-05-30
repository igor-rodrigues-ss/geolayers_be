#!-*-coding:utf-8-*-


import pytest

from tests.conftest import url_for
from src.apps.health.db import DBHealth
from src.apps.health.celery import CeleryHealth
from src.apps.health.cache import CacheHealth
from src.config import UP, DOWN, NO_CACHE_SERVICE, DB_SERVICE, CELERY_SERVICE
from src.apps.health.health_status import HealthStatus


SOME_MSG = 'SOME_MSG'


async def hstatus_up(self):
    return HealthStatus(UP)


async def hstatus_down(self):
    return HealthStatus(DOWN, msg=SOME_MSG)


@pytest.fixture
def celery_up(monkeypatch):
    monkeypatch.setattr(CeleryHealth, 'hstatus', hstatus_up)


@pytest.fixture
def celery_down(monkeypatch):
    monkeypatch.setattr(CeleryHealth, 'hstatus', hstatus_down)


@pytest.fixture
def cache_up(monkeypatch):
    monkeypatch.setattr(CacheHealth, 'hstatus', hstatus_up)

@pytest.fixture
def cache_down(monkeypatch):
    monkeypatch.setattr(CacheHealth, 'hstatus', hstatus_down)


@pytest.fixture
def db_down(monkeypatch):
    monkeypatch.setattr(DBHealth, 'hstatus', hstatus_down)


class TestHealthCheckDOWN:

    def test_get_success(self, client, celery_down, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        assert resp.status_code == 200

    def test_get_app_down(self, client, celery_down, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()
        assert data['status'] == DOWN

    def test_get_db_down(self, client, db_down, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['status'] == DOWN
        assert data['checks'][0]['name'] == DB_SERVICE
        assert data['checks'][0]['status'] == DOWN

    def test_get_celery_down(self, client, celery_down, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['status'] == DOWN
        assert data['checks'][1]['name'] == CELERY_SERVICE
        assert data['checks'][1]['status'] == DOWN

    def test_get_cache_down(self, client, celery_up, cache_down):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['status'] == DOWN
        assert data['checks'][2]['name'] == NO_CACHE_SERVICE
        assert data['checks'][2]['status'] == DOWN



