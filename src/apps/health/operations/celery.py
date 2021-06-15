#!-*-coding:utf-8-*-

from src.apps.health.operations.ihealth import IHealth
from src.celery.app import celery_app
from src.config import UP, DOWN, CELERY_SERVICE
from src.apps.health.entities.health_status import HealthStatus


class CeleryHealth(IHealth):

    def __init__(self):
        self._inspect = celery_app.control.inspect()

    def name(self) -> str:
        return CELERY_SERVICE

    async def hstatus(self) -> HealthStatus:
        ping = self._inspect.ping()

        if ping is None:
            return HealthStatus(DOWN, 'Sem resposta do celery')

        for worker_name, ping in ping.items():
            if ping['ok'] != 'pong':
                return HealthStatus(DOWN, 'Sem resposta do celery')
        return HealthStatus(UP)

    async def details(self) -> dict:
        availability = self._inspect.ping()
        stats = self._inspect.stats()
        registered_tasks = self._inspect.registered()
        active_tasks = self._inspect.active()
        scheduled_tasks = self._inspect.scheduled()
        result = {
            'disponibilidade': availability,
            'stats': stats,
            'tasks_registradas': registered_tasks,
            'tasks_ativas': active_tasks,
            'tasks_agendadas': scheduled_tasks
        }
        return result