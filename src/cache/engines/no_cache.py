#!-*-coding:utf-8-*-

from src.config import CACHE_EXPTIME, NO_CACHE_SERVICE
from src.cache.icache import ICache
from src.framework.log import LOGGER


class NoCache(ICache):

    def name(self) -> str:
        return NO_CACHE_SERVICE

    def client(self) -> object:
        return None

    async def get(self, key: bytes) -> bytes:
        LOGGER.warning('Cache desabilitado.')
        return None

    async def set(self, key: bytes, val: bytes, exptime: int = CACHE_EXPTIME):
        return None

    async def delete(self, key: bytes) -> object:
        return None