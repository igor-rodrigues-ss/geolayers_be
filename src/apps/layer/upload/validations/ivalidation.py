#!-*-coding:utf-8-*-

from abc import ABC, abstractmethod


class IValidation(ABC):

    @abstractmethod
    def validate(self):
        pass