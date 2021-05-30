#!-*-coding:utf-8-*-

from fastapi import status
from tests.conftest import url_for
from tests.rest.health.fixtures import cache_name_memcached
from src.config import DB_SERVICE, MEM_CACHED_SERVICE, CELERY_SERVICE


class TestHealthService:

    def test_get_sucess(self, client):
        url = url_for('health_services')
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_check_services(self, client, cache_name_memcached):
        url = url_for('health_services')
        resp = client.get(url)

        assert DB_SERVICE in resp.json()
        assert MEM_CACHED_SERVICE in resp.json()
        assert CELERY_SERVICE in resp.json()
