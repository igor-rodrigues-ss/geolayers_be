#!-*-coding:utf-8-*-


from src.cache.engines.memcached import MemCachedCache
from src.cache.icache import ICache
from src.config import CACHE_EXPTIME


class CacheSingleton(ICache):

    def __init__(self, engine: ICache):
        self._engine = engine

    def update_engine(self, engine: ICache):
        self._engine = engine

    def client(self) -> object:
        return self._engine

    async def get(self, key: bytes) -> bytes:
        # LOGGER.info('Cache desabilitado.')
        print('Cache desabilitado.')
        return await self._engine.get(key)

    async def set(self, key: bytes, val: bytes, exptime: int = CACHE_EXPTIME):
        await self._engine.set(key, val, exptime)

    async def delete(self, key: bytes):
        await self._engine.delete(key)


CACHE = CacheSingleton(MemCachedCache())
