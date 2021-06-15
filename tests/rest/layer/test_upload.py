#!-*-coding:utf-8-*-

from fastapi import status
from tests.conftest import url_for
from src.db.models import t_save_layer
from src.db.sync_connection import SYNC_DB
from src.celery.worker_exceptions import GeometryOutOfBrazil
from src.config import WORKER_STATUS_SUCCESS, WORKER_STATUS_FAILURE
from tests.constants import FILL, FILE_NAME, PATH, COLOR, FPATH_OUT_OF_BRAZIL, NAME_OUT_OF_BRAZIL


class TestUploadlayer:

    def setup_method(self):
        with SYNC_DB.engine().connect() as conn:
            conn.execute(t_save_layer.delete())

    def _exc_msg(self):
        exc = GeometryOutOfBrazil()
        exc_cls = exc.__class__.__name__
        return f'{exc_cls}: {str(exc)}'

    def test_post_success_204(self, client):
        resp = client.post(
            url_for('upload_layer'),
            files={'file': (FILE_NAME, open(PATH, "rb"))},
            data={'color': COLOR, 'fill': FILL}
        )
        assert resp.status_code == status.HTTP_204_NO_CONTENT

    def test_post_success_check_dadta(self, client):
        _ = client.post(
            url_for('upload_layer'),
            files={'file': (FILE_NAME, open(PATH, "rb"))},
            data={'color': COLOR, 'fill': FILL}
        )
        with SYNC_DB.engine().connect() as conn:
            stmt = t_save_layer.select()
            task = conn.execute(stmt).fetchone()
            assert task.status == WORKER_STATUS_SUCCESS
            assert task.detail == ''

    def test_post_error_status_204(self, client):
        resp = client.post(
            url_for('upload_layer'),
            files={'file': (NAME_OUT_OF_BRAZIL, open(FPATH_OUT_OF_BRAZIL, "rb"))},
            data={'color': COLOR, 'fill': FILL}
        )
        assert resp.status_code == status.HTTP_204_NO_CONTENT

    def test_post_error_check_data(self, client):
        _ = client.post(
            url_for('upload_layer'),
            files={'file': (NAME_OUT_OF_BRAZIL, open(FPATH_OUT_OF_BRAZIL, "rb"))},
            data={'color': COLOR, 'fill': FILL}
        )
        with SYNC_DB.engine().connect() as conn:
            stmt = t_save_layer.select()
            task = conn.execute(stmt).fetchone()
            assert task.status == WORKER_STATUS_FAILURE
            assert task.detail == self._exc_msg()
