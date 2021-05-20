#!-*-coding:utf-8-*-

import pytest
from fastapi import status
from tests.utils import is_uuid
from tests.conftest import url_for
from src.db.sync_connection import SYNC_DB
# from src.models import t_layer
from tests.constants import FILL, FILE_NAME, PATH, COLOR, NAME


@pytest.fixture(scope='module', autouse=True)
def create_layer(client):

    with SYNC_DB.engine().connect() as conn:
        # TODO: passar este sql para ORM
        conn.execute('truncate table layer cascade;')

    client.post(
        url_for('upload_layer'),
        files={'file': (FILE_NAME, open(PATH, "rb"))},
        data={'color': COLOR, 'fill': FILL}
    )


class TestListLayers:

    def test_get_success(self, client):
        url = url_for('get_layers')
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_layers_qtt(self, client):
        url = url_for('get_layers')
        resp = client.get(url)
        assert len(resp.json()) == 1

    def test_get_layers_data(self, client):
        resp = client.get(url_for('get_layers'))
        data = resp.json()
        lyr = list(data.values())[0]

        assert lyr['nome'] == NAME
        assert lyr['color'] == COLOR
        assert lyr['fill'] is FILL
        assert lyr['show'] is False

    def test_get_layers_check_id(self, client):
        resp = client.get(url_for('get_layers'))
        data = resp.json()
        id_lyr = list(data.keys())[0]
        assert is_uuid(id_lyr)
