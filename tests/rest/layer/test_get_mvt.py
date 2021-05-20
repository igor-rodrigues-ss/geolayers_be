#!-*-coding:utf-8-*-

import pytest
from fastapi import status
from tests.utils import path_test_file
from tests.conftest import url_for
from src.db.default_conn_celery import engine
from src.models import t_layer
from tests.constants import FILL, FILE_NAME, PATH, COLOR


@pytest.fixture(scope='module', autouse=True)
def created_layer(client):
    client.post(
        url_for('upload_layer'),
        files={'file': (FILE_NAME, open(PATH, "rb"))},
        data={'color': COLOR, 'fill': FILL}
    )
    with engine.connect() as conn:
        row = conn.execute(t_layer.select())
        row = row.fetchone()
        return {'id': row.id}


class TestGetMVT:

    def test_get_mvt_success(self, client, created_layer):
        id_lyr = created_layer['id']
        resp = client.get(
            url_for('get_mvt_layer', **{'layer_id': id_lyr, 'z': 7, 'x': 46, 'y': 66, 'fmt': 'pbf'})
        )
        assert resp.status_code == status.HTTP_200_OK

    def test_get_mvt_data(self, client, created_layer):
        id_lyr = created_layer['id']
        resp = client.get(
            url_for('get_mvt_layer', **{'layer_id': id_lyr, 'z': 7, 'x': 46, 'y': 66, 'fmt': 'pbf'})
        )
        assert resp.content != b''

    def test_get_mvt_empty(self, client, created_layer):
        id_lyr = created_layer['id']
        resp = client.get(
            url_for('get_mvt_layer', **{'layer_id': id_lyr, 'z': 1, 'x': 1, 'y': 1, 'fmt': 'pbf'})
        )
        assert resp.content == b''
