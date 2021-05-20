# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, ForeignKey, Integer, JSON, MetaData, String, Table, Text, text
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2.types import Geometry

metadata = MetaData()


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


t_layer = Table(
    'layer', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('nome', String(256), nullable=False)
)


t_spatial_ref_sys = Table(
    'spatial_ref_sys', metadata,
    Column('srid', Integer, primary_key=True),
    Column('auth_name', String(256)),
    Column('auth_srid', Integer),
    Column('srtext', String(2048)),
    Column('proj4text', String(2048)),
    CheckConstraint('(srid > 0) AND (srid <= 998999)')
)


t_layer_properties = Table(
    'layer_properties', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('layer_id', ForeignKey('layer.id'), nullable=False),
    Column('propertie', JSON, nullable=False)
)


t_styles = Table(
    'styles', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('id_layer', ForeignKey('layer.id'), nullable=False),
    Column('color', String(20), nullable=False),
    Column('fill', Boolean, nullable=False)
)


t_layer_geometries = Table(
    'layer_geometries', metadata,
    Column('id', UUID, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('layer_id', ForeignKey('layer.id'), nullable=False),
    Column('propertie_id', ForeignKey('layer_properties.id'), nullable=False),
    Column('geom', Geometry(from_text='ST_GeomFromEWKT', name='geometry')),
    CheckConstraint('st_srid(geom) = 4674')
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
