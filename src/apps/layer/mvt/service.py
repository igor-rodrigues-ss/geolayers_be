#!-*-coding:utf-8-*-


from src.apps.layer.mvt.tile import Tile
from src.apps.layer.mvt.envelope import Envelope
from src.apps.layer.mvt.envelope_sql import EnvelopeSQL
from src.apps.layer.mvt.repository.tile_repo import TileRepository
# from src.caching.caching upload CACHE
# from src.config upload MAP_MVT_LAYERS
# from src.framework.exceptions upload CamadaMVTNaoRegistrada


class MVTService:

    def __init__(self, lyr_name: str, z: int, x: int, y: int, fmt: str):
        self._lyr_name = lyr_name
        self._z = z
        self._x = x
        self._y = y
        self._fmt = fmt

    async def tiles(self):
        # mvt_lyr_data = MAP_MVT_LAYERS.get(self._lyr_name, None)

        # if mvt_lyr_data is None:
            # raise CamadaMVTNaoRegistrada(self._lyr_name)
            # raise Exception('AA')

        tile = Tile(self._z, self._x, self._y, self._fmt)
        tile.is_valid()

        tr = TileRepository(EnvelopeSQL(Envelope(tile), {}))
        return await tr.get_one()

    # async def _cached_tiles(self, unique_key: str) -> bytes:
    #     pbf = await CACHE.get(unique_key)
    #
    #     if pbf is None:
    #         pbf = await self._tiles()
    #         await CACHE.set(unique_key, pbf)
    #         return pbf
    #
    #     print('Usando cache!')
    #     return pbf

    # async def tiles(self):
    #
    #     def _gen(pbf) -> bytes:
    #         yield pbf
    #
    #     cache_key = bytes(str(f'{self._lyr_name}_{self._z}_{self._x}_{self._y}_{self._fmt}'), encoding='utf-8')
    #     pbf = await self._cached_tiles(cache_key)
    #
    #     return _gen(pbf)
