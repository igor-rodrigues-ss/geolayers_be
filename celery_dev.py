#!-*-coding:utf-8-*-

import os
import dev_envs as _


os.system('poetry run celery -A src.celery.app worker --loglevel=info')