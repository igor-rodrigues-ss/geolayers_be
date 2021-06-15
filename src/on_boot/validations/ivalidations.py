#!-*-coding:utf-8-*-

from abc import ABC, abstractmethod


class IBootValidation(ABC):

    @abstractmethod
    async def validate(self):
        pass
