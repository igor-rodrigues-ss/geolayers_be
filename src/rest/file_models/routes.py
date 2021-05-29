#!-*-coding:utf-8-*-

from src.rest.file_models.views import FileModelsList, FileModelsDownload
from fastapi import APIRouter


router = APIRouter()
lv = FileModelsList()
dv = FileModelsDownload()


router.get('', name='files_model_list')(lv.get)
router.get('/{fname}', name='files_model_download')(dv.get)

