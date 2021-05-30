#!-*-coding:utf-8-*-


from fastapi import status
from tests.conftest import url_for, INEXISTING_SERVICE
from tests.rest.health.fixtures import (
    db_detail, celery_detail, cache_detail, cache_name_memcached
)
from tests.conftest import SOME_DICT_INFO
from src.config import DB_SERVICE, MEM_CACHED_SERVICE, CELERY_SERVICE
from src.framework.exc_codes import INEXISTING_SERVICE


class TestHealthServiceDetail:

    def test_get_db_info_success(self, client):
        url = url_for('health_detail', service_name=DB_SERVICE)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_db_detail(self, client, db_detail):
        url = url_for('health_detail', service_name=DB_SERVICE)
        resp = client.get(url)
        assert resp.json() == SOME_DICT_INFO

    def test_get_celery_info_success(self, client, celery_detail):
        url = url_for('health_detail', service_name=CELERY_SERVICE)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_celery_detail(self, client, celery_detail):
        url = url_for('health_detail', service_name=CELERY_SERVICE)
        resp = client.get(url)
        assert resp.json() == SOME_DICT_INFO

    def test_get_cache_info_success(self, client, cache_detail, cache_name_memcached):
        url = url_for('health_detail', service_name=MEM_CACHED_SERVICE)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_cache_detail(self, client, cache_detail, cache_name_memcached):
        url = url_for('health_detail', service_name=MEM_CACHED_SERVICE)
        resp = client.get(url)
        assert resp.json() == SOME_DICT_INFO

    def test_get_inexisting_service_status_400(self, client):
        url = url_for('health_detail', service_name=INEXISTING_SERVICE)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_inexisting_service_msg(self, client):
        url = url_for('health_detail', service_name=INEXISTING_SERVICE)
        resp = client.get(url)
        assert bool(resp.json()['detail']['msg'])

    def test_get_inexisting_service_code(self, client):
        url = url_for('health_detail', service_name=INEXISTING_SERVICE)
        resp = client.get(url)
        assert resp.json()['detail']['code'] == INEXISTING_SERVICE
