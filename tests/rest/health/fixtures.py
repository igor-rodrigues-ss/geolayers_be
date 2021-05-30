#!-*-coding:utf-8-*-

import pytest
from src.apps.health.db import DBHealth
from src.apps.health.celery import CeleryHealth
from src.apps.health.cache import CacheHealth
from src.apps.health.health_status import HealthStatus
from src.config import UP, DOWN, MEM_CACHED_SERVICE
from tests.conftest import SOME_MSG, SOME_DICT_INFO


async def hstatus_up(self):
    return HealthStatus(UP)


async def hstatus_down(self):
    return HealthStatus(DOWN, msg=SOME_MSG)


def name_memcached(self):
    return MEM_CACHED_SERVICE


async def info_dict(self):
    return SOME_DICT_INFO


@pytest.fixture
def cache_name_memcached(monkeypatch):
    monkeypatch.setattr(CacheHealth, 'name', name_memcached)


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


@pytest.fixture
def db_detail(monkeypatch):
    monkeypatch.setattr(DBHealth, 'details', info_dict)


@pytest.fixture
def celery_detail(monkeypatch):
    monkeypatch.setattr(CeleryHealth, 'details', info_dict)


@pytest.fixture
def cache_detail(monkeypatch):
    monkeypatch.setattr(CacheHealth, 'details', info_dict)
