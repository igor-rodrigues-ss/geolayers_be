#!-*-coding:utf-8-*-

import os
from uuid import UUID
from src.config import ROOT_DIR


def is_uuid(val: str):
    try:
        _ = UUID(val, version=4)
    except ValueError:
        return False
    return True


def path_test_file(fname: str):
    return os.path.join(
        ROOT_DIR, 'fixtures', 'test_files', fname
    )
