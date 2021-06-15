#!-*-coding:utf-8-*-

import time
from src.config import MAX_ATTEMPS, SLEEP_FOR_NEXT_ATTEMPT
from src.db.async_connection import ASYNC_DB
from src.on_boot.validations.ivalidations import IBootValidation
from src.framework.log import LOGGER


class DBConnectionValidation(IBootValidation):

    async def validate(self) -> bool:
        valid = False
        for i in range(MAX_ATTEMPS):
            try:
                valid = await ASYNC_DB.test_connection()
            except Exception as ex:
                LOGGER.warning(
                    'Impossível se conectar a base de dados. '
                    f'Tente novamente em alguns segundos.\nExc: {str(ex)}\n'
                )

                if i + 1 == MAX_ATTEMPS:
                    raise ex

                time.sleep(SLEEP_FOR_NEXT_ATTEMPT)
            else:
                break
        return valid
