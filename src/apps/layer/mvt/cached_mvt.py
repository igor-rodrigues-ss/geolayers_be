#!-*-coding:utf-8-*-

from src.cache.cache import CACHE
from src.apps.layer.mvt.iservice import ILayerMVTService


class CachedLayerMVT(ILayerMVTService):

    _mvt: ILayerMVTService

    def __init__(self, mvt_cls: ILayerMVTService):
        self._mvt_cls = mvt_cls

    def __call__(self, *args, **kwargs):
        self._mvt = self._mvt_cls(*args, **kwargs)
        return self

    async def tiles(self, layer_id: str, z: int, x: int, y: int, fmt: str) -> bytes:
        unique_key = bytes(
            str(f'{layer_id}_{z}_{x}_{y}_{fmt}'), encoding='utf-8'
        )
        pbf = await CACHE.get(unique_key)

        if pbf is None:
            pbf = await self._mvt.tiles(layer_id, z, x, y, fmt)
            await CACHE.set(unique_key, pbf)
            return pbf

        print('Usando Cache')
        return pbf