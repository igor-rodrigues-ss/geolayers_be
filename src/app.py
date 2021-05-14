#!-*-coding:utf-8-*-

from fastapi import FastAPI
from src.db.default_connection import DB_DEFAULT
from fastapi.middleware.cors import CORSMiddleware
from src.rest.layer.routes import router as layer_router
from src.cache.cache import CACHE
from src.cache.engines.no_cache import NoCache

# TODO: criar middleware de try except
# TODO: criar uma página de download para arquivos de teste
# TODO: ajustar exceptios dos tiles
# TODO: refatorar código e services
# TODO: ajustar comentários de MVT
# TODO: passar o upload para messageria
# TODO: adicionar upload de geojson e geopackage
# TODO: ajustar logs
# TODO: criar docker para deploy
# TODO: criar autenticação
# TODO: ajustar mensagens de erros http no front
# TODO: criar desenho com a arquitetura do back (MEMCACHED, FastAPI, CELERY e RABBIT)
# TODO: FRONT - ajustar o changeLayerVisibility para passar somente os dados necessários (id e show)

# poetry run sqlacodegen postgresql://postgres:123456@localhost:5432/geolayer --noclasses > models.py
# docker run --name memcached -p 11211:11211 -d memcached m^Ccached --threads 4 -m 1024
# Dados Abertos - https://forest-gis.com/download-de-shapefiles/

app = FastAPI()


app.include_router(
    layer_router,
    prefix="/layer", tags=["Layer"],
    responses={404: {"description": "Not found"}},
)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event('startup')
async def startup():
    await DB_DEFAULT.connect()
    try:
        await CACHE.set(b'teste', b'1')
        await CACHE.delete(b'teste')
        print('Cache Habilitado')
    except Exception as ex:
        print('Cache Desabilitado')
        CACHE.update_engine(NoCache())

