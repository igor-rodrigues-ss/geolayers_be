#!-*-coding:utf-8-*-


import os
import dev_envs as _


os.system('pipenv run uvicorn src.app:app --reload')