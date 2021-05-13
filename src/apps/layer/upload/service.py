#!-*-coding:utf-8-*-
import json
from fastapi import UploadFile

from src.apps.layer.upload.repository import LayerImportRepo
from src.apps.layer.upload.shapefile import Shapefile


class LayerUpload:

    async def save(self, file: UploadFile):
        sf = Shapefile(file)
        repo = LayerImportRepo(sf._file.filename, await sf.features())
        await repo.save()
