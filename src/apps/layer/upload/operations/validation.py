#!-*-coding:utf-8-*-

from osgeo.ogr import Geometry
from src.apps.layer.upload.operations.shapefile import Shapefile
from src.celery.worker_exceptions import GeometryOutOfBrazil


class Validation:

    _br_geom: Geometry
    _shape: Shapefile

    def __init__(self, br_geom: Geometry, shape: Shapefile):
        self._br_geom = br_geom
        self._shape = shape

    def validate(self):
        valid = self._br_geom.Intersect(self._shape.geometry())
        if not valid:
            raise GeometryOutOfBrazil()
