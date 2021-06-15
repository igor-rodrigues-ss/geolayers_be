#!-*-coding:utf-8-*-


from typing import Generator
from vectorio.compress import Zip
from vectorio.vector import Shapefile as ShapefileVIO, ShapefileCompressed
from osgeo.ogr import CreateGeometryFromJson, Geometry


class Shapefile:

    _shape: ShapefileCompressed

    def __init__(self, path: str):
        self._shape = ShapefileCompressed(
            ShapefileVIO(path, search_encoding_exception=False), compress_engine=Zip()
        )

    def features(self) -> Generator[str, None, None]:
        return self._shape.features()

    def geometry(self) -> Geometry:
        return CreateGeometryFromJson(self._shape.geometry_collection())

