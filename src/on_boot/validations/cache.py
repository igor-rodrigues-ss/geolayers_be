#!-*-coding:utf-8-*-

from src.cache.cache import CACHE
from src.on_boot.validations.ivalidations import IBootValidation


class CacheValidation(IBootValidation):

    async def validate(self) -> bool:
        try:
            await CACHE.set(b'teste', b'1')
            await CACHE.delete(b'teste')
            print('Cache Habilitado')
            return True
        except Exception as ex:
            print('Cache Desabilitado')
            return False