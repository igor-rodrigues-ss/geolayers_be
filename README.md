
# GeoLayers Backend

## Async Rest API using Python and FastAPI For Processing Geospatial Layers

### Tools:
- Python3.8
- FastAPI
- PostgreSQL / PostGIS
- RabbitMQ + Celery
- Docker / Docker-Compose
- MemCached
- Vectorio
- SQLAlchemy
- pipenv

### Features
- Shapefile Upload
- Mapbox Vector Tile Generator

### Requirements
- Python3.8
- Pipenv
- GDAL 3.0.4
- Docker

### Dev Mode
```shell
cd /path/to/geolayers_be

# Preparing environment and install all dependencies
pipenv install

# Starting MemCached service
docker run --name memcached -p 11211:11211 --rm -d memcached memcached --threads 4 -m 1024 

# Starting RabbitMQ service
docker run -d --rm --net=host rabbitmq

# Starting worker
pipenv run celery_dev.py 

# Starting worker monitoring service
pipenv run celery -A src.celery.app worker --loglevel=info

# Starting API
pipenv run dev.py

# Access: http://localhost:8000/docs
```

