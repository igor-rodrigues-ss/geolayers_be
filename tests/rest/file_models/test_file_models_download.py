#!-*-coding:utf-8-*-

import os
from fastapi import status
from tests.conftest import url_for
from src.config import FILE_MODELS_PATH
from src.framework.exc_codes import INEXISTING_FILE_MODEL


INEXISTING_FILE = 'abc.zip'


class TestFileModelsDownload:

    def test_get_success(self, client):
        for fname in os.listdir(FILE_MODELS_PATH):
            url = url_for('file_models_download', fname=fname)
            resp = client.get(url)
            assert resp.status_code == status.HTTP_200_OK

    def test_download_file(self, client, tmp_path):
        for fname in os.listdir(FILE_MODELS_PATH):
            print(f'>>> Testing download: {fname}')
            url = url_for('file_models_download', fname=fname)
            resp = client.get(url)
            outpath = tmp_path / fname

            with open(outpath, 'wb') as f:
                f.write(resp.content)

            assert os.path.exists(outpath)

    def test_download_inexisting_file_status(self, client):
        url = url_for('file_models_download', fname=INEXISTING_FILE)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_400_BAD_REQUEST

    def test_download_inexisting_file_code(self, client):
        url = url_for('file_models_download', fname=INEXISTING_FILE)
        resp = client.get(url)
        assert bool(resp.json()['detail']['msg'])

    def test_download_inexisting_file_code(self, client):
        url = url_for('file_models_download', fname=INEXISTING_FILE)
        resp = client.get(url)
        assert resp.json()['detail']['code'] == INEXISTING_FILE_MODEL
