



# TODO: deixar uma estrutura de banco vazia salva (deixar uma estrtura para ambiente de DEV documentada)
# TODO: Documentar neste README o Deploy
# TODO: criar desenho com a arquitetura do back (MEMCACHED, FastAPI, CELERY e RABBIT)


# TODO: criar parâmetro do script de deploy para para criar base de dados inicial no deploy da aplicação
# TODO: criar validação para arquivos que não possuem extensão
# TODO: Adicionar uma ferramenta de log para monitoramento em tempo real (Prometheus ou Grafana)
# TODO: criar autenticação
# TODO: adicionar upload de geojson e geopackage

# TODO: FRONT - ajustar o changeLayerVisibility para passar somente os dados necessários (id e show)
# TODO: ajustar tipagens do front e do back


# docker run --name memcached -p 11211:11211 --rm -d memcached memcached --threads 4 -m 1024
# docker run -d --rm --net=host rabbitmq
# poetry run celery -A src.celery.app worker --loglevel=info
# Dados Abertos - https://forest-gis.com/download-de-shapefiles/