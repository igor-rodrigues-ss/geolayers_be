#!-*-coding:utf-8-*-


from src.rest.health.views import (
    HealthView, HeathServicesView, HealthServicesDetail
)
from src.rest.health.schemas import health_check, list_services, service_detail
from fastapi import APIRouter


router = APIRouter()
health = HealthView()
serv = HeathServicesView()
details = HealthServicesDetail()


router.get(
    '',
    name='health_check',
    responses={200: {'content': {'application/json': {'example': health_check}}}}
)(health.get)

router.get(
    '/services',
    name='health_services',
    responses={200: {'content': {'application/json': {'example': list_services}}}}
)(serv.get)

router.get(
    '/{service_name}',
    name='health_detail',
    responses={200: {'content': {'application/json': {'example': service_detail}}}}
)(details.get)

