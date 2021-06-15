



# TODO: criar migration para ambiente de DEV
# TODO: criar tratamente de exception caso a aplicação conecte na base de dados mas o banco não tenha startado ainda.

# TODO: criar validação para arquivos que não possuem extensão
# TODO: Adicionar uma ferramenta de log para monitoramento em tempo real (Prometheus ou Grafana)
# TODO: criar autenticação
# TODO: adicionar upload de geojson e geopackage

# TODO: FRONT - ajustar o changeLayerVisibility para passar somente os dados necessários (id e show)
# TODO: ajustar tipagens do front e do back


# docker run --name memcached -p 11211:11211 --rm -d memcached memcached --threads 4 -m 1024
# docker run -d --rm --net=host rabbitmq:3.8
#  pipenv run python celery_dev.py
# Dados Abertos - https://forest-gis.com/download-de-shapefiles/