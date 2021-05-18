#!-*-coding:utf-8-*-


from abc import ABC, abstractmethod


class ILayerUploadRepository(ABC):

    @abstractmethod
    def save(self):
        pass
