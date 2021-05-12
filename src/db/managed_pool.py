#!-*-coding:utf-8-*-

import asyncio
from contextlib import asynccontextmanager
# from src.framework.exceptions upload ImpossivelObterConexaoValida
# from src.framework.log upload LOGGER
# from src.config upload MAX_ATTEMPT_PRE_VALIDATE_CONN
# TODO: verificar a necessidade de: DB_ACQUIRE_TIMEOUT


class ManagedPool:

    def __init__(self, db_pool, db_name: str, max_attempt: int = 10):
        self.db_pool = db_pool
        self.db_name = db_name
        self.max_attempt = max_attempt

    async def acquire(self):
        conn = None

        for attempt in range(1, self.max_attempt + 1):
            if attempt > 1:
                pass
                # LOGGER.warning(f'\n')
                # LOGGER.warning(f'Revalidando Conexão: {attempt}ª Tentativa.')

            try:
                # conn = await asyncio.wait_for(self.db_pool.acquire(), timeout=DB_ACQUIRE_TIMEOUT)
                conn = await self.db_pool.acquire()
                res = await conn.execute('SELECT 1')
                res = await res.fetchone()
                return conn
            
            # except asyncio.exceptions.TimeoutError as ex:
            #     exc = ex
            #     if bool(conn):
            #         await self.release(conn)

            except Exception as ex:
                exc = ex

                if bool(conn):
                    # LOGGER.warning(f'>>> Connection obj: {conn.connection}')
                    # LOGGER.warning(f'>>> conn.closed: {conn.closed}')
                    # LOGGER.warning(f'>>> Pool Size: {self.db_pool.size}')
                    await self.release(conn)

                if conn is None:
                    # LOGGER.warning(f'>>> Connection obj: None')
                    continue

                #'server closed the connection unexpectedly' not in str(exc).lower():
                # if conn.closed == 0:
                #     # Esta condicional server para lançar as exceptions de connexoes válidas
                #     raise exc

        if attempt == self.max_attempt:
            raise Exception('Ex')
            # raise ImpossivelObterConexaoValida(str(exc), self.db_name)

    async def release(self, conn):
        
        try:
            await self.db_pool.release(conn)

            # LOGGER.info('\n\n')
            # LOGGER.info(f'>>> Pool Size: {self.db_pool.size}')
            # LOGGER.info(f'>>> conn.closed (engine) >> {conn.closed}')
            # LOGGER.info(f'>>> conn.connection (wrapper) >> {conn.connection}', )
            # LOGGER.info(f'>>> conn.connection.closed (wrapper.close) >> {conn.connection.closed}')
            # LOGGER.info(f'>>> conn.connection._conn (psycopg) >> {conn.connection._conn.closed}')
            # LOGGER.info(f'>>> Release.')
            # LOGGER.info('\n\n')

        except Exception as exc:
            pass
            # pass

            # LOGGER.warning(f'>>>>>>>>>>>>>>>>>>>>>>>>>> Exc on release <<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            # LOGGER.warning(f'>>> Pool Size: {self.db_pool.size}')
            # LOGGER.warning(f'>>> EXC: {str(exc)}')
            
            if bool(conn):
                pass
                # LOGGER.warning(f'>>> Connection obj: {conn.connection}')
                # LOGGER.warning(f'>>> conn.closed (engine) >> {conn.closed}')
                # LOGGER.warning(f'>>> conn.connection (wrapper) >> {conn.connection}', )
                # LOGGER.warning(f'>>> conn.connection.closed (wrapper.close) >> {conn.connection.closed}')
                # LOGGER.warning(f'>>> conn.connection._conn (psycopg) >> {conn.connection._conn.closed}')


@asynccontextmanager
async def managed_pool(db_pool, db_name: str, max_attempt: int = 10):
    mp = ManagedPool(db_pool, db_name, max_attempt)
    conn = await mp.acquire()
    try:
        yield conn
    except Exception as exc:
        await mp.release(conn)
        raise exc    
    await mp.release(conn)
