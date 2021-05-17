#!-*-coding:utf-8-*-


import os
from fastapi import UploadFile
from src.apps.layer.upload.celery.task import save_layer


class LayerUpload:

    async def _save(self, file):
        fpath = f'/tmp/{file.filename}'
        with open(fpath, 'wb') as f:
            cont = await file.read()
            f.write(cont)
        return fpath

    def _layer_name(self, path):
        fname = os.path.basename(path)
        fname_splited = fname.split('.')
        return '.'.join(fname_splited[:-1])

    async def save(self, file: UploadFile, color: str, fill: bool):
        path = await self._save(file)
        lyr_name = self._layer_name(path)
        task = save_layer.delay(lyr_name, path, color, fill)
        print({
            'task': task.id,
            'status': task.status
        })


        # TODO: salver id da task no banco para consultar o status da inserção