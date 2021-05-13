#!-*-coding:utf-8-*-

from fastapi import UploadFile, File

from src.apps.layer.list.repository import LayerListRepo
from src.apps.layer.mvt.service import MVTService
from fastapi.responses import StreamingResponse
from src.apps.layer.upload.service import LayerUpload


class LayerView:

    async def get_mvt(self, layer_id: str, z: int, x: int, y: int, fmt: str):
        mvt = MVTService(layer_id, z, x, y, fmt)
        headers = {"Access-Control-Allow-Origin": "*", "Content-type": "application/vnd.mapbox-vector-tile"}

        def _gen(pbf) -> bytes:
            yield pbf

        return StreamingResponse(
            _gen(await mvt.tiles()), headers=headers
        )

    async def post(self, file: UploadFile = File(...)):
        return await LayerUpload().save(file)

    async def list_all(self):
        return await LayerListRepo().list_all()
