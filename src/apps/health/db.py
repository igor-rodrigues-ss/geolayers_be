#!-*-coding:utf-8-*-

from src.apps.health.ihealth import IHealth
from src.db.async_connection import ASYNC_DB
from src.config import UP, DOWN
from src.framework.log import LOGGER
from src.apps.health.health_status import HealthStatus


class DBHealth(IHealth):

    def name(self) -> str:
        return 'DB Geolayers'

    async def hstatus(self) -> HealthStatus:
        try:
            valid = await ASYNC_DB.test_connection()
        except Exception as ex:
            LOGGER.error(str(ex))
            return HealthStatus(DOWN, str(ex))
        else:
            if valid:
                return HealthStatus(UP)
            return HealthStatus(DOWN, 'Resultado inesperado da validação de conexões.')