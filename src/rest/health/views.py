#!-*-coding:utf-8-*-

from src.apps.health.service import HealthService


class HealthCheckView:

    async def get(self):
        return await HealthService().check()


class HeathServicesView:

    async def get(self):
        return HealthService().services_names()


class HealthServicesDetail:

    async def get(self, service_name: str):
        return await HealthService().details(
            service_name
        )
