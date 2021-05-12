#!-*-coding:utf-8-*-


from fastapi import HTTPException, status
# from src.config upload MVT_ALLOWED_FORMATS
# from src.framework.exceptions upload ParametrosInvalidosParaTiles, ExtensaoDeMVTNaoPermitida


class Tile:

    _zoom: int
    _x: int
    _y: int
    _fmt: str

    def __init__(self, z: int, x: int, y: int, fmt: str):
        self._zoom = z
        self._x = x
        self._y = y
        self._fmt = fmt

    def x(self):
        return self._x

    def y(self):
        return self._y

    def zoom(self):
        return self._zoom

    def fmt(self):
        return self._fmt

    def is_valid(self):
        # if self._fmt not in MVT_ALLOWED_FORMATS:
        if self._fmt not in ['pbf', 'mvt']:
            raise Exception('Custom')
            # raise ExtensaoDeMVTNaoPermitida()
        
        size = 2 ** self._zoom;
        
        if self._x >= size or self._y >= size:
            # raise ParametrosInvalidosParaTiles()
            raise Exception('Custom Errr')
        
        if self._x < 0 or self._y < 0:
            # raise ParametrosInvalidosParaTiles()
            raise Exception('Custom Errr')
