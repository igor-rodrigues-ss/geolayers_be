#!-*-coding:utf-8-*-

from fastapi import APIRouter
from src.rest.tasks.views import TasksSaveLayer
from src.rest.tasks.schemas import list_tasks


router = APIRouter()
view = TasksSaveLayer()


router.get(
    '',
    name='list_all_tasks_save_layer',
    responses={200: {'content': {'application/json': {'example': list_tasks}}}}
)(view.list_all)
