#!-*-coding:utf-8-*-

from abc import ABC, abstractmethod


class ILayerMVTService(ABC):

    @abstractmethod
    async def tiles(self, layer_id: str, z: int, x: int, y: int, fmt: str) -> bytes:
        pass
