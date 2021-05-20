#!-*-coding:utf-8-*-

from fastapi import status
from tests.conftest import url_for
from tests.constants import FILL, FILE_NAME, PATH, COLOR


class TestUploadlayer:

    def test_post_204(self, client):
        resp = client.post(
            url_for('upload_layer'),
            files={'file': (FILE_NAME, open(PATH, "rb"))},
            data={'color': COLOR, 'fill': FILL}
        )
        assert resp.status_code == status.HTTP_204_NO_CONTENT
