#!-*-coding:utf-8-*-

from fastapi import HTTPException, status
from src.config import MVT_ALLOWED_FORMATS
from src.framework.exc_codes import INVALID_TILE_PARAMS, EXT_MVT_NOT_ALLOWED


class MVTExtensionNotAllowed(HTTPException):

    def __init__(self):
        msg = f'Extensão mvt não suportada. Extensões permitidas "{", ".join(MVT_ALLOWED_FORMATS)}"'
        code = EXT_MVT_NOT_ALLOWED
        exc = ''

        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'msg': msg,
                'code': code,
                'exc': exc
            }
        )


class InvalidTileParams(HTTPException):

    def __init__(self):
        msg = 'Parâmetros inválidos para construção do tile.'
        code = INVALID_TILE_PARAMS
        exc = ''

        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'msg': msg,
                'code': code,
                'exc': exc
            }
        )
