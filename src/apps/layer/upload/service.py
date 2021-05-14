#!-*-coding:utf-8-*-
import json
from fastapi import UploadFile

from src.apps.layer.upload.repository import LayerImportRepo
from src.apps.layer.upload.shapefile import Shapefile


class LayerUpload:

    async def save(self, file: UploadFile, color: str, fill: bool):
        sf = Shapefile(file)
        repo = LayerImportRepo(sf._file.filename, await sf.features(), color, fill)
        await repo.save()
