#!-*-coding:utf-8-*-

from src.apps.layer.mvt.cached_service import CachedLayerMVT
from src.apps.layer.mvt.iservice import ILayerMVTService
from src.apps.layer.mvt.operations.tile import Tile
from src.apps.layer.mvt.operations.envelope import Envelope
from src.apps.layer.mvt.repository.repository import LayerMVTRepository


@CachedLayerMVT
class LayerMVTService(ILayerMVTService):

    async def tiles(self, layer_id: str, z: int, x: int, y: int, fmt: str):
        tile = Tile(z, x, y, fmt)
        tile.is_valid()
        tr = LayerMVTRepository(layer_id, Envelope(tile))
        return await tr.get_one()
