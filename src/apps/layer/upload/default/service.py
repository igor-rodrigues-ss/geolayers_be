#!-*-coding:utf-8-*-


from fastapi import UploadFile
from src.apps.layer.upload.default.repository import LayerImportRepo
from src.apps.layer.upload.default.shapefile import Shapefile


class LayerUpload:

    def _layer_name(self, file: UploadFile):
        fname_splited = file.filename.split('.')
        return '.'.join(fname_splited[:-1])

    async def save(self, file: UploadFile, color: str, fill: bool):
        sf = Shapefile(file)
        repo = LayerImportRepo(
            self._layer_name(file), await sf.features(), color, fill
        )
        await repo.save()
