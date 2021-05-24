# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, ForeignKey, JSON, MetaData, String, Table, text
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2.types import Geometry

metadata = MetaData()


t_layer = Table(
    'layer', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('nome', String(256), nullable=False),
    schema='layers'
)


t_properties = Table(
    'properties', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('layer_id', ForeignKey('layers.layer.id'), nullable=False),
    Column('properties', JSON, nullable=False),
    schema='layers'
)


t_styles = Table(
    'styles', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('layer_id', ForeignKey('layers.layer.id'), nullable=False),
    Column('color', String(20), nullable=False),
    Column('fill', Boolean, nullable=False),
    schema='layers'
)


t_geometries = Table(
    'geometries', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('layer_id', ForeignKey('layers.layer.id'), nullable=False),
    Column('properties_id', ForeignKey('layers.properties.id'), nullable=False),
    Column('geom', Geometry(from_text='ST_GeomFromEWKT', name='geometry')),
    CheckConstraint('st_srid(geom) = 4674'),
    schema='layers'
)
# coding: utf-8
from sqlalchemy import Column, MetaData, String, Table, Text
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()


t_save_layer = Table(
    'save_layer', metadata,
    Column('id', UUID, primary_key=True),
    Column('layer_name', String(256)),
    Column('status', String(20)),
    Column('detail', Text),
    schema='tasks'
)
