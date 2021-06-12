#!-*-coding:utf-8-*-

from src.config import MVT_ALLOWED_FORMATS
from src.framework.exceptions import MVTExtensionNotAllowed, InvalidTileParams


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
        if self._fmt not in MVT_ALLOWED_FORMATS:
            raise MVTExtensionNotAllowed()
        
        size = 2 ** self._zoom;
        
        if self._x >= size or self._y >= size:
            raise InvalidTileParams()

        if self._x < 0 or self._y < 0:
            raise InvalidTileParams()
