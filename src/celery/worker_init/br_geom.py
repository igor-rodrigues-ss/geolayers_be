#!-*-coding:utf-8-*-

from osgeo.ogr import CreateGeometryFromWkt
from src.config import BR_GEOM_PATH


class BRGeom:

    def geom(self):
        with open(BR_GEOM_PATH) as f:
            return CreateGeometryFromWkt(f.read())