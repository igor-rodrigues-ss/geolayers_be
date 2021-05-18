#!-*-coding:utf-8-*-


from typing import Generator
from vectorio.compress import Zip
from vectorio.vector import Shapefile as ShapefileVIO, ShapefileCompressed


class Shapefile:

    _path: str

    def __init__(self, path: str):
        self._path = path

    def features(self) -> Generator[str, None, None]:
        shape = ShapefileCompressed(
            ShapefileVIO(self._path, search_encoding_exception=False), compress_engine=Zip()
        )
        return shape.features()
