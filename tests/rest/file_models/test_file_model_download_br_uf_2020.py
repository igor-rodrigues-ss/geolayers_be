#!-*-coding:utf-8-*-

import json
from tests.conftest import url_for
from vectorio.vector import Shapefile, ShapefileCompressed
from vectorio.compress import Zip


TEST_FNAME = 'BR_UF_2020.zip'
BR_UF_2020_GEOM_LEN = 27


class TestFileModelDownloadBrUf2020:

    def test_download_valid_file(self, client, tmp_path):
        url = url_for('file_models_download', fname=TEST_FNAME)
        resp = client.get(url)
        outpath = tmp_path / TEST_FNAME

        with open(outpath, 'wb') as f:
            f.write(resp.content)

        shp = ShapefileCompressed(Shapefile(str(outpath)), compress_engine=Zip())
        geomc = json.loads(shp.geometry_collection())
        assert len(geomc['geometries']) == BR_UF_2020_GEOM_LEN
