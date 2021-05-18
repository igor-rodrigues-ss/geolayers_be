#!-*-coding:utf-8-*-


from fastapi import UploadFile
from src.apps.layer.upload.task import save_layer
from src.apps.layer.upload.sent_file import SentFile


class LayerUpload:

    async def save(self, file: UploadFile, color: str, fill: bool):
        sfile = SentFile(file)
        path = await sfile.save()
        save_layer.delay(sfile.name(), path, color, fill)
