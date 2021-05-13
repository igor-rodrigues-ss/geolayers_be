#!-*-coding:utf-8-*-

from fastapi import UploadFile
from vectorio.vector import Shapefile as ShapefileVIO, ShapefileCompressed
from vectorio.compress import Zip


class Shapefile:

    def __init__(self, file: UploadFile):
        self._file = file

    async def _save(self):
        fpath = f'/tmp/{self._file.filename}'
        with open(fpath, 'wb') as f:
            cont = await self._file.read()
            f.write(cont)
        return fpath

    async def features(self):
        fpath = await self._save()
        shape = ShapefileCompressed(
            ShapefileVIO(fpath, search_encoding_exception=False), compress_engine=Zip()
        )
        return shape.features()