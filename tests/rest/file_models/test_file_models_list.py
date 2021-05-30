#!-*-coding:utf-8-*-

import os
from fastapi import status
from tests.conftest import url_for
from src.config import FILE_MODELS_PATH


class TestFileModelsList:

    def test_get_success(self, client):
        url = url_for('file_models_list')
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_data(self, client):
        url = url_for('file_models_list')
        resp = client.get(url)
        assert os.listdir(FILE_MODELS_PATH) == resp.json()
