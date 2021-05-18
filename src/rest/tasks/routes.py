#!-*-coding:utf-8-*-




from fastapi import APIRouter, status
from src.rest.tasks.views import TasksSaveLayer

router = APIRouter()
view = TasksSaveLayer()


router.get('', name='get_all_saving_layers')(view.list_all)
