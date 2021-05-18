#!-*-coding:utf-8-*-

from fastapi import UploadFile


class SentFile:

    def __init__(self, file: UploadFile):
        self._file = file

    def name(self):
        fname = self._file.filename
        fname_splited = fname.split('.')
        return '.'.join(fname_splited[:-1])

    async def save(self):
        fpath = f'/tmp/{self._file.filename}'
        with open(fpath, 'wb') as f:
            cont = await self._file.read()
            f.write(cont)
        return fpath
