#!-*-coding:utf-8-*-

from osgeo.ogr import Geometry
from src.apps.layer.upload.operations.shapefile import Shapefile
from src.apps.layer.upload.validations.ivalidation import IValidation
from src.celery.worker_exceptions import GeometryOutOfBrazil
from osgeo.ogr import CreateGeometryFromJson


class GeomInsideBrazil(IValidation):

    _br_geom: Geometry
    _shape: Shapefile

    def __init__(self, br_geom: Geometry, shape: Shapefile):
        self._br_geom = br_geom
        self._shape = shape

    def validate(self):
        for geom_gj in self._shape.geometries():
            geom = CreateGeometryFromJson(geom_gj)
            valid = self._br_geom.Intersect(geom)
            if not valid:
                raise GeometryOutOfBrazil()
