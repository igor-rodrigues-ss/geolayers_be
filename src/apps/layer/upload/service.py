#!-*-coding:utf-8-*-
import json
from fastapi import UploadFile
from vectorio.vector import Shapefile, ShapefileCompressed
from vectorio.compress import Zip
from src.apps.layer.upload.repository import save_feature


class LayerUpload:

    async def save(self, file: UploadFile):
        fpath = f'/tmp/{file.filename}'
        with open(fpath, 'wb') as f:
            cont = await file.read()
            f.write(cont)

        shape = ShapefileCompressed(Shapefile(fpath, search_encoding_exception=False), compress_engine=Zip())

        for i, feat in enumerate(shape.features()):
            await save_feature(file.filename, json.loads(feat))
            print(i)

        return {}
