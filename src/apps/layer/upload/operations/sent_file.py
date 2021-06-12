#!-*-coding:utf-8-*-

import os
from fastapi import UploadFile
from src.config import UPLOADED_FILE_PATH


class SentFile:

    def __init__(self, file: UploadFile):
        self._file = file

    def name(self):
        fname = self._file.filename
        fname_splited = fname.split('.')
        return '.'.join(fname_splited[:-1])

    async def save(self):
        fpath = os.path.join(UPLOADED_FILE_PATH, self._file.filename)
        with open(fpath, 'wb') as f:
            cont = await self._file.read()
            f.write(cont)
        return fpath
