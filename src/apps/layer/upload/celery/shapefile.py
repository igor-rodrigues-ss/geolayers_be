#!-*-coding:utf-8-*-

from fastapi import UploadFile
from vectorio.vector import Shapefile as ShapefileVIO, ShapefileCompressed
from vectorio.compress import Zip

class Shapefile:

    def __init__(self, path: str):
        self._path = path

    def features(self):
        shape = ShapefileCompressed(
            ShapefileVIO(self._path, search_encoding_exception=False), compress_engine=Zip()
        )
        return shape.features()