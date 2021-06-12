#!-*-coding:utf-8-*-


from fastapi import UploadFile
from src.apps.layer.upload.task import save_layer
from src.apps.layer.upload.operations.sent_file import SentFile


class LayerUploadService:

    async def save(self, file: UploadFile, color: str, fill: bool):
        sf = SentFile(file)
        path = await sf.save()
        save_layer.delay(sf.name(), path, color, fill)
