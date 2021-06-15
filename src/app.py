#!-*-coding:utf-8-*-

import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.on_boot.validations.cache import CacheValidation
from src.on_boot.validations.db_connection import DBConnectionValidation
from src.rest.layer.routes import router as layer_router
from src.rest.tasks.routes import router as tasks_router
from src.rest.health.routes import router as health_router
from src.rest.file_models.routes import router as files_models_router
from src.cache.cache import CACHE
from src.cache.engines.no_cache import NoCache
from src.middlewares.try_except import try_except
from src.framework.log import LOGGER
from src.config import UPLOADED_FILE_PATH


def create_app():

    app = FastAPI()
    app.logger = LOGGER

    # Middlewares ====================================
    app.middleware("http")(try_except)
    app.add_middleware(
        CORSMiddleware, allow_origins=["*"],
        allow_credentials=True, allow_methods=["*"],
        allow_headers=["*"],
    )

    # Events ===========================================
    @app.on_event('startup')
    async def startup():
        cache_valid = await CacheValidation().validate()
        if not cache_valid:
            CACHE.update_engine(NoCache())

        if not os.path.exists(UPLOADED_FILE_PATH):
            os.makedirs(UPLOADED_FILE_PATH)

        conn_valid = await DBConnectionValidation().validate()
        if conn_valid:
            LOGGER.info('Connexão realizada com sucesso!!!!')
        else:
            sys.exit('Impossível criar uma conexão válida com a base de dados.')




    # Routes ==============================================
    app.include_router(
        layer_router,
        prefix="/layer", tags=["Layer"],
        responses={404: {"description": "Not found"}},
    )
    app.include_router(
        tasks_router,
        prefix="/tasks", tags=["Tasks"],
        responses={404: {"description": "Not found"}},
    )
    app.include_router(
        health_router,
        prefix="/health", tags=["Health"],
        responses={404: {"description": "Not found"}},
    )
    app.include_router(
        files_models_router,
        prefix="/file-models", tags=["File Models"],
        responses={404: {"description": "Not found"}},
    )

    return app


app = create_app()

