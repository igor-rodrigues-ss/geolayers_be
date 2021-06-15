#!-*-coding:utf-8-*-

import pytest
from fastapi import status
from src.db.models import t_save_layer
from src.db.sync_connection import SYNC_DB
from tests.conftest import url_for
from src.config import WORKER_STATUS_SUCCESS
from tests.utils import is_uuid
from tests.constants import FILL, FILE_NAME, PATH, COLOR, NAME


@pytest.fixture(scope='module', autouse=True)
def create_layer(client):
    with SYNC_DB.engine().connect() as conn:
        conn.execute(t_save_layer.delete())

    client.post(
        url_for('upload_layer'),
        files={'file': (FILE_NAME, open(PATH, "rb"))},
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
