#!-*-coding:utf-8-*-

from src.apps.health.service import Service


class HealthCheckView:

    async def get(self):
        return await Service().check()


class HeathServicesView:

    async def get(self):
        return Service().services_names()


class HealthServicesDetail:

    async def get(self, service_name: str):
        return await Service().details(
            service_name
        )
