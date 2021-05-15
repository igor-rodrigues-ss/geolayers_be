#!-*-coding:utf-8-*-

import traceback
from fastapi import Request, HTTPException, status
from starlette.responses import JSONResponse
from src.framework.exc_codes import UNEXPECTED_ERROR
from src.framework.log import LOGGER


async def try_except(request: Request, call_next):
    try:
        response = await call_next(request)
    except Exception as exc:
        if not isinstance(exc, HTTPException):
            exc_name = exc.__class__.__name__
            LOGGER.error(f'\n{traceback.format_exc()}')
            return JSONResponse({
                'detail': {
                    'msg': f'Erro inesperado. Por favor, entre em contato com o administrador da aplicação.',
                    'code': UNEXPECTED_ERROR,
                    'exc': f'{exc_name}: {str(exc)}'
                }
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return response