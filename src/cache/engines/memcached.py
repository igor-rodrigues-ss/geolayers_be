#!-*-coding:utf-8-*-


from src.config import (
    ENVS, CACHE_POOL_SIZE_MIN, CACHE_POOL_SIZE_MAX
)

from aiomemcached import Client
from src.config import CACHE_EXPTIME
from src.cache.icache import ICache


class MemCachedCache(ICache):

    def __init__(self):
        self._client = Client(
            host=ENVS.CACHE_HOST, port=int(ENVS.CACHE_PORT),
            pool_minsize=CACHE_POOL_SIZE_MIN, pool_maxsize=CACHE_POOL_SIZE_MAX
        )

    def client(self) -> object:
        return self._client

    async def get(self, key: bytes) -> bytes:
        val, _ = await self._client.get(key)
        return val

    async def set(self, key: bytes, val: bytes, exptime: int = CACHE_EXPTIME):
        await self._client.set(key, val, exptime=exptime)

    async def delete(self, key: bytes):
        await self._client.delete(key)
