#!-*-coding:utf-8-*-

from abc import abstractmethod, ABC
from src.config import CACHE_EXPTIME


class ICache(ABC):

    @abstractmethod
    def name(self) -> str:
        return

    @abstractmethod
    def client(self) -> object:
        pass

    @abstractmethod
    def get(self, key: bytes) -> bytes:
        pass

    @abstractmethod
    def set(self, key: bytes, val: bytes, exptime: int = CACHE_EXPTIME):
        pass

    @abstractmethod
    async def delete(self, key: bytes) -> object:
        pass