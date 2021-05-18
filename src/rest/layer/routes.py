#!-*-coding:utf-8-*-

from fastapi import APIRouter, status

from src.rest.layer.views import LayerView

router = APIRouter()
lv = LayerView()


router.post(
    '/upload', name='create_layer', status_code=status.HTTP_204_NO_CONTENT
)(lv.post)
router.get('/{layer_id}/mvt/{z}/{x}/{y}.{fmt}', name='get_mvt_layer')(lv.get_mvt)
router.get('', name='get_layers')(lv.list_all)

