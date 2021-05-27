#!-*-coding:utf-8-*-


from src.rest.health.views import HealthView, HeathServicesView, HealthServicesDetail
from fastapi import APIRouter, status


router = APIRouter()
health = HealthView()
serv = HeathServicesView()
details = HealthServicesDetail()


router.get('', name='health_check')(health.get)
router.get('/services', name='health_services')(serv.get)
router.get('/{service_name}', name='health_detail')(details.get)


