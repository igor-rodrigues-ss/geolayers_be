#!-*-coding:utf-8-*-

from src.config import WORKER_STATUS_SUCCESS, WORKER_STATUS_FAILURE, WORKER_STATUS_PENDING

list_tasks = [
  {
    "id": "UUID",
    "layer_name": "str",
    "status": f"{WORKER_STATUS_SUCCESS} | {WORKER_STATUS_FAILURE} | {WORKER_STATUS_PENDING}",
    "detail": "str"
  }
]