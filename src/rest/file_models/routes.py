#!-*-coding:utf-8-*-

from src.rest.file_models.views import FileModelsList, FileModelsDownload
from fastapi import APIRouter
from src.rest.file_models.schemas import list_file_models
from starlette.responses import FileResponse


router = APIRouter()
lv = FileModelsList()
dv = FileModelsDownload()


router.get(
    '',
    name='files_model_list',
    responses={200: {'content': {'application/json': {'example': list_file_models}}}}

)(lv.get)

router.get(
    '/{fname}',
    name='files_model_download',
    response_class=FileResponse,
    responses={200: {'content': {'application/octet-stream': {'example': 'bytes'}}}}
)(dv.get)

