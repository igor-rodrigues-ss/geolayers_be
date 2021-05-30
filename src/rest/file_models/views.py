#!-*-coding:utf-8-*-


from starlette.responses import FileResponse
from src.apps.file_models.service import FileModelsService


class FileModelsList:

    def get(self):
        return FileModelsService().list_all()


class FileModelsDownload:

    def get(self, fname: str):
        fdata = FileModelsService().fdata(fname)
        return FileResponse(
            fdata['path'],
            media_type='application/octet-stream',
            filename=fdata['name']
        )
