#!-*-coding:utf-8-*-

from tests.conftest import url_for
import pytest

from src.apps.health.celery import CeleryHealth
from src.apps.health.cache import CacheHealth
from src.config import UP, NO_CACHE_SERVICE, DB_SERVICE, CELERY_SERVICE
from src.apps.health.health_status import HealthStatus


async def hstatus_up(self):
    return HealthStatus(UP)


@pytest.fixture
def celery_up(monkeypatch):
    monkeypatch.setattr(CeleryHealth, 'hstatus', hstatus_up)


@pytest.fixture
def cache_up(monkeypatch):
    monkeypatch.setattr(CacheHealth, 'hstatus', hstatus_up)


class TestHealthCheckUP:

    def test_get_success(self, client, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        assert resp.status_code == 200

    def test_get_app_up(self, client, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()
        assert data['status'] == UP

    def test_get_db_up(self, client, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['checks'][0]['name'] == DB_SERVICE
        assert data['checks'][0]['status'] == UP

    def test_get_celery_up(self, client, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['checks'][1]['name'] == CELERY_SERVICE
        assert data['checks'][1]['status'] == UP

    def test_get_cache_up(self, client, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['checks'][2]['name'] == NO_CACHE_SERVICE
        assert data['checks'][2]['status'] == UP



