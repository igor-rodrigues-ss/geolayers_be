
from typing import Dict, Union, Any, List

from src.apps.health.operations.db import DBHealth
from src.apps.health.operations.ihealth import IHealth
from src.apps.health.operations.cache import CacheHealth
from src.apps.health.operations.celery import CeleryHealth
from src.config import UP, DOWN
from src.framework.exceptions import InexistingService


class HealthService:

    _services: Dict[str, IHealth]

    def __init__(self):
        services = [
            DBHealth(), CeleryHealth(), CacheHealth()
        ]
        self._services = {obj.name(): obj for obj in services}

    async def _app_status(self):
        for _, service in self._services.items():
            hs = await service.hstatus()
            if hs.status == DOWN:
                return DOWN
        return UP

    async def check(self) -> Dict[str, Union[List[dict], Any]]:
        checks = []
        for _, service in self._services.items():
            checks.append(
               await service.check()
            )
        return {
            'status': await self._app_status(),
            'checks': checks
        }

    def services_names(self):
        return list(self._services.keys())

    async def details(self, service_name: str):
        service = self._services.get(service_name, None)
        if service is None:
            raise InexistingService()
        return await service.details()