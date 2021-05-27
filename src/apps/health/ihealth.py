#!-*-coding:utf-8-*-


from abc import ABC, abstractmethod
from src.apps.health.health_status import HealthStatus


class IHealth(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    async def hstatus(self) -> HealthStatus:
        return

    async def check(self) -> dict:
        hs = await self.hstatus()
        if hs.msg is None:
            return {
                'name': self.name(),
                'status': hs.status
            }
        return {
            'name': self.name(),
            'status': hs.status,
            'msg': hs.msg
        }

    async def details(self) -> dict:
        return {}
