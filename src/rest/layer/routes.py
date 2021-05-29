#!-*-coding:utf-8-*-

from fastapi import APIRouter, status
from src.rest.layer.views import LayerView
from src.rest.layer.schemas import list_layers
from fastapi.responses import StreamingResponse


router = APIRouter()
lv = LayerView()


router.post(
    '/upload', name='upload_layer', status_code=status.HTTP_204_NO_CONTENT
)(lv.post)

router.get(
    '/{layer_id}/mvt/{z}/{x}/{y}.{fmt}',
    name='get_mvt_layer',
    response_class=StreamingResponse,
    responses={
        200: {
            "content": {
                "application/vnd.mapbox-vector-tile": {
                    "example": "bytes"
                }
            },
            "description": "Retorna um tile .pbf.",
        }
    }
)(lv.get_mvt)

router.get(
    '',
    name='get_layers',
    responses={200: {'content': {'application/json': {"example": list_layers}}}}
)(lv.list_all)
