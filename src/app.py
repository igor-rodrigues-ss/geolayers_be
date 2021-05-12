from src.db.default_connection import DB_DEFAULT
from src.apps.layer.upload.service import LayerUpload
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File, FastAPI
from src.apps.layer.mvt.service import MVTService
from fastapi.responses import StreamingResponse



app = FastAPI()


origins = [
    "*"
]

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


@app.on_event("startup")
async def startup():
    print('START')
    await DB_DEFAULT.connect()


@app.get("/mvt/{z}/{x}/{y}.{fmt}")
async def mvt(z: int, x: int, y: int, fmt: str):
    mvt = MVTService('l1', z, x, y, fmt)
    headers = {"Access-Control-Allow-Origin": "*", "Content-type": "application/vnd.mapbox-vector-tile"}

    def _gen(pbf) -> bytes:
        yield pbf

    return StreamingResponse(
        _gen(await mvt.tiles()), headers=headers
    )


@app.post("/import")
async def importing(file: UploadFile = File(...)):
    return await LayerUpload().save(file)

# poetry run sqlacodegen postgresql://postgres:123456@localhost:5432/geolayer --noclasses > models.py
# poetry add uvicorn app:app --reload