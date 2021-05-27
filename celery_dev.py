#!-*-coding:utf-8-*-

import os
import dev_envs as _


os.system('pipenv run celery -A src.celery.app worker --loglevel=info')

# src.apps.layer.upload.task.save_layer
# os.system('pipenv run python')