#!-*-coding:utf-8-*-

import pytest
from fastapi import status
from tests.utils import is_uuid
from tests.conftest import url_for


PATH = '/home/igor/igor/pos-graduacao/data/BR_UF_2020.zip'
COLOR = '#222'
FILL = True
NAME = 'BR_UF_2020'
FILE_NAME = f'{NAME}.zip'


@pytest.fixture(scope='module', autouse=True)
def create_layer(client):
    client.post(
        url_for('upload_layer'),
        files={'file': (FILE_NAME, open(PATH, "rb")),},
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
