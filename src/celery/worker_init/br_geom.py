#!-*-coding:utf-8-*-

from osgeo.ogr import CreateGeometryFromWkt


class BRGeom:

    def geom(self):
        # TODO: mudar este arquivo de lugar
        with open('/home/igor/br_geom.wkt') as f:
            return CreateGeometryFromWkt(f.read())