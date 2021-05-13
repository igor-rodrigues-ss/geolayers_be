#!-*-coding:utf-8-*-

from fastapi import FastAPI
from src.db.default_connection import DB_DEFAULT
from fastapi.middleware.cors import CORSMiddleware
from src.rest.layer.routes import router as layer_router


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


# poetry run sqlacodegen postgresql://postgres:123456@localhost:5432/geolayer --noclasses > models.py