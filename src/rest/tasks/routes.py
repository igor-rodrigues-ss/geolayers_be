#!-*-coding:utf-8-*-




from fastapi import APIRouter, status
from src.rest.tasks.views import TasksSaveLayer

router = APIRouter()
view = TasksSaveLayer()


router.get('', name='list_all_tasks_save_layer')(view.list_all)
