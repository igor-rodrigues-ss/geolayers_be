
# GeoLayers Backend

## Async Rest API using Python and FastAPI For Processing Geospatial Layers

### OS
- Linux

### Used Tools:
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
- Mapbox Vector Tile (MVT) Generator

### Requirements
- Python3.8
- Pipenv
- GDAL 3.0.4
- Docker

### Development Mode
```shell
cd /path/to/geolayers_be

# Preparing environment and install all dependencies
pipenv install

# Starting MemCached service
docker run --name memcached -p 11211:11211 --rm -d memcached memcached --threads 4 -m 1024 

# Starting RabbitMQ service
docker run -d --rm --net=host rabbitmq

# Starting worker
pipenv run python celery_dev.py 

# Starting worker monitoring service
pipenv run celery -A src.celery.app worker --loglevel=info

# Starting API
pipenv run python dev.py

# Access: http://localhost:8000/docs
```

## Deploy

- All the artifacts for application deploy (for both frontend and backend) are in [geolayer_deploy](https://github.com/igor-rodrigues-ss/geolayers_deploy) project.

- The next tutorial will deploy frontend and backend already integrateds.

### Requirements
- git: 2.25.1
- Docker: 20.10.6, build 370c289
- Docker-compose: 1.28.5, build c4eb3a1f

```shell
git clone https://github.com/igor-rodrigues-ss/geolayers_deploy
cd geolayers_deploy
./deploy

# after deploying go to: http://localhost:3000
```