#!-*-coding:utf-8-*-

from fastapi import status
from tests.conftest import url_for


PATH = '/home/igor/igor/pos-graduacao/data/BR_UF_2020.zip'


class TestUpload:

    def test_post_204(self, client):
        resp = client.post(
            url_for('upload_layer'),
            files={'file': ("file.zip", open(PATH, "rb"))},
            data={'color': '#222', 'fill': 'true'}
        )
        assert resp.status_code == status.HTTP_204_NO_CONTENT

