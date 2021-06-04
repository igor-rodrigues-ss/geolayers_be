#!-*-coding:utf-8-*-


from fastapi import UploadFile, File, Form, Response, status
from src.apps.layer.list.repository import LayerListRepository
from src.apps.layer.mvt.service import LayerMVTService
from fastapi.responses import StreamingResponse
from src.apps.layer.upload.service import LayerUploadService


class LayerView:

    async def get_mvt(self, layer_id: str, z: int, x: int, y: int, fmt: str):
        mvt = LayerMVTService()
        headers = {"Access-Control-Allow-Origin": "*", "Content-type": "application/vnd.mapbox-vector-tile"}
        tiles = await mvt.tiles(layer_id, z, x, y, fmt)

        def gen(pbf) -> bytes:
            yield pbf

        return StreamingResponse(gen(tiles), headers=headers)

    async def post(
        self, file: UploadFile = File(...), color: str = Form(...), fill: bool = Form(...)
    ):
        await LayerUploadService().save(file, color, fill)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    async def list_all(self):
        return await LayerListRepository().list_all()
