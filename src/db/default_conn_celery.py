from sqlalchemy import create_engine
from src.config import ENVS


engine = create_engine(
    f'postgresql+psycopg2://{ENVS.DB_USER}:{ENVS.DB_PASSWORD}@{ENVS.DB_HOST}:{ENVS.DB_PORT}/{ENVS.DB_NAME}'
)