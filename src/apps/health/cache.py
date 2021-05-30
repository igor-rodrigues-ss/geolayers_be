#!-*-coding:utf-8-*-
from src.apps.health.health_status import HealthStatus
from src.apps.health.ihealth import IHealth
from src.cache.cache import CACHE
from src.config import UP, DOWN
from src.framework.log import LOGGER


class CacheHealth(IHealth):

    def name(self) -> str:
        return CACHE.name()

    async def hstatus(self) -> HealthStatus:
        try:
            await CACHE.set(b'teste', b'health')
        except Exception as ex:
            LOGGER.error(str(ex))
            return HealthStatus(DOWN, str(ex))
        else:
            await CACHE.delete(b'teste')
            return HealthStatus(UP)

