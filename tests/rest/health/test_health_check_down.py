#!-*-coding:utf-8-*-


from tests.conftest import url_for, SOME_MSG
from src.config import DOWN, MEM_CACHED_SERVICE, DB_SERVICE, CELERY_SERVICE
from tests.rest.health.fixtures import (
    celery_up, celery_down, cache_up, cache_down, db_down, cache_name_memcached
)
from fastapi import status


class TestHealthCheckDOWN:

    def test_get_success(self, client, celery_down, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

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

    def test_get_db_down_msg(self, client, db_down, celery_up, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['checks'][0]['msg'] == SOME_MSG

    def test_get_celery_down(self, client, celery_down, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['status'] == DOWN
        assert data['checks'][1]['name'] == CELERY_SERVICE
        assert data['checks'][1]['status'] == DOWN
        assert data['checks'][1]['msg'] == SOME_MSG

    def test_get_celery_down_msg(self, client, celery_down, cache_up):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['checks'][1]['msg'] == SOME_MSG

    def test_get_cache_down(self, client, celery_up, cache_down, cache_name_memcached):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()

        assert data['status'] == DOWN
        assert data['checks'][2]['name'] == MEM_CACHED_SERVICE
        assert data['checks'][2]['status'] == DOWN

    def test_get_cache_down_msg(self, client, celery_up, cache_down):
        url = url_for('health_check')
        resp = client.get(url)
        data = resp.json()
        assert data['checks'][2]['msg'] == SOME_MSG
