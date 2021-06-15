#!-*-coding:utf-8-*-

from typing import Union
from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.engine import Engine


class IConnection(ABC):

    @abstractmethod
    def engine(self) -> Union[AsyncEngine, Engine]:
        pass

