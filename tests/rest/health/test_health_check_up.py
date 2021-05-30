#!-*-coding:utf-8-*-


from tests.conftest import url_for
from src.config import UP, MEM_CACHED_SERVICE, DB_SERVICE, CELERY_SERVICE
from src.apps.health.health_status import HealthStatus
from tests.rest.health.fixtures import (
    celery_up, cache_up, cache_name_memcached
)
from fastapi import status


class TestHealthCheckUP:

    def test_get_success(self, client, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

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

    def test_get_cache_up(self, client, celery_up, cache_up, cache_name_memcached):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['checks'][2]['name'] == MEM_CACHED_SERVICE
        assert data['checks'][2]['status'] == UP
