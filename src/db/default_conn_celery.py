from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/geolayer')