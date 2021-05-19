#!-*-coding:utf-8-*-

import pytest
from uuid import UUID
from fastapi import status
from tests.conftest import url_for
from src.config import WORKER_STATUS_SUCCESS
from tests.utils import is_uuid

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


class TestTaskSaveLayer:

    def test_list_success(self, client):
        resp = client.get(url_for('list_all_tasks_save_layer'))
        assert resp.status_code == status.HTTP_200_OK

    def test_list_check_data(self, client):
        resp = client.get(url_for('list_all_tasks_save_layer'))
        task_data = resp.json()[0]
        assert task_data['layer_name'] == NAME
        assert task_data['status'] == WORKER_STATUS_SUCCESS

    def test_list_check_id(self, client):
        resp = client.get(url_for('list_all_tasks_save_layer'))
        task_data = resp.json()[0]
        assert is_uuid(task_data['id'])
