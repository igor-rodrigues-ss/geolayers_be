#!-*-coding:utf-8-*-

import os
from src.config import FILE_MODELS_PATH
from src.framework.exceptions import InexistingFileModel


class FileModelsService:

    def list_all(self):
        return os.listdir(FILE_MODELS_PATH)

    def fdata(self, fname: str):
        fpath = os.path.join(FILE_MODELS_PATH, fname)

        if not os.path.exists(fpath):
            raise InexistingFileModel()

        fname = os.path.basename(fpath)

        return {
            'name': fname, 'path': fpath
        }