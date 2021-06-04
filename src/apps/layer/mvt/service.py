#!-*-coding:utf-8-*-

from src.apps.layer.mvt.cached_mvt import CachedLayerMVT
from src.apps.layer.mvt.iservice import ILayerMVTService
from src.apps.layer.mvt.tile import Tile
from src.apps.layer.mvt.envelope import Envelope
from src.apps.layer.mvt.envelope_sql import EnvelopeSQL
from src.apps.layer.mvt.repository import LayerMVTRepository


@CachedLayerMVT
class LayerMVTService(ILayerMVTService):

    async def tiles(self, layer_id: str, z: int, x: int, y: int, fmt: str):
        tile = Tile(z, x, y, fmt)
        tile.is_valid()
        tr = LayerMVTRepository(EnvelopeSQL(layer_id, Envelope(tile), {}))
        return await tr.get_one()
