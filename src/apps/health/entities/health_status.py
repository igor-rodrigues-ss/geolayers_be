#!-*-coding:utf-8-*-


from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class HealthStatus:
    status: str  # UP, DOWN
    msg: Optional[str] = None
