#!-*-coding:utf-8-*-

import os
from src.config import FILE_MODELS_PATH
from fastapi.exceptions import HTTPException
from starlette.responses import FileResponse


class FileModelsList:

    async def get(self):
        return os.listdir(FILE_MODELS_PATH)


class FileModelsDownload:

    async def get(self, fname: str):
        fpath = os.path.join(FILE_MODELS_PATH, fname)

        if not os.path.exists(fpath):
            raise HTTPException(status_code=400)

        fname = os.path.basename(fpath)

        return FileResponse(
            fpath, media_type='application/octet-stream', filename=fname
        )
