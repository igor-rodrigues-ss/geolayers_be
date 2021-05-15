#!-*-coding:utf-8-*-

import logging
import sys
from loguru import logger
from src.config import FORMAT_LOG
from src.config import LOG_PATH


class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: 'CRITICAL',
        40: 'ERROR',
        30: 'WARNING',
        20: 'INFO',
        10: 'DEBUG',
        0: 'NOTSET',
    }

    def _get_log_level(self, record: logging.LogRecord):
        try:
            return logger.level(record.levelname).name
        except AttributeError:
            return self.loglevel_mapping[record.levelno]

    def emit(self, record: logging.LogRecord):
        level = self._get_log_level(record)

        SHOW_SERVER_FUNCTION = 6

        logger.opt(
            depth=SHOW_SERVER_FUNCTION, exception=record.exc_info
        ).log(level, record.getMessage())  # escrevendo log
        # record.getMessage() - sys.stdout da aplicação


class CustomizeLogger:

    @classmethod
    def make_logger(cls):
        LEVEL = 'INFO'
        logger.remove()  # Removendo os logs do fim do processamento do uvicorn
        logger.add(
            sys.stdout, enqueue=True, backtrace=True,
            level=LEVEL.upper(),
            format=FORMAT_LOG
        )
        logger.add(
            LOG_PATH, enqueue=True, backtrace=True,
            level=LEVEL.upper(),
            format=FORMAT_LOG
        )
        # Capturando as saídas de logs do uvicorn e fastapi
        for _log in ['uvicorn', 'uvicorn.access', 'uvicorn.error', 'fastapi']:
            _logger = logging.getLogger(_log)
            _logger.handlers = [InterceptHandler()]

        return logger
