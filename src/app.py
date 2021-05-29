#!-*-coding:utf-8-*-

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.rest.layer.routes import router as layer_router
from src.rest.tasks.routes import router as tasks_router
from src.rest.health.routes import router as health_router
from src.rest.file_models.routes import router as files_models_router
from src.cache.cache import CACHE
from src.cache.engines.no_cache import NoCache
from src.middlewares.try_except import try_except
from src.framework.log import LOGGER
from src.config import UPLOADED_FILE_PATH

# TODO: criar testes unitários do health check
# TODO: deixar uma estrutura de banco vazia salva

# TODO: criar validação para arquivos que não possuem extensão
# TODO: Adicionar uma ferramenta de log para monitoramento em tempo real (Prometheus ou Grafana)

# TODO: criar autenticação
# TODO: adicionar upload de geojson e geopackage
# TODO: criar desenho com a arquitetura do back (MEMCACHED, FastAPI, CELERY e RABBIT)
# TODO: FRONT - ajustar o changeLayerVisibility para passar somente os dados necessários (id e show)
# TODO: ajustar tipagens do front e do back


# docker run --name memcached -p 11211:11211 --rm -d memcached memcached --threads 4 -m 1024
# docker run -d --rm --net=host rabbitmq
# poetry run celery -A src.celery.app worker --loglevel=info
# Dados Abertos - https://forest-gis.com/download-de-shapefiles/


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
        try:
            await CACHE.set(b'teste', b'1')
            await CACHE.delete(b'teste')
            print('Cache Habilitado')
        except Exception as ex:
            print('Cache Desabilitado')
            CACHE.update_engine(NoCache())

        if not os.path.exists(UPLOADED_FILE_PATH):
            os.makedirs(UPLOADED_FILE_PATH)

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

