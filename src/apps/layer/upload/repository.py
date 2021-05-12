#!-*-coding:utf-8-*-

import json
from src.db.default_connection import DB_DEFAULT
from geoalchemy2.functions import ST_GeomFromGeoJSON, ST_SetSRID
from src.models import *


async def save_feature(fname, feat):
        async with DB_DEFAULT.pool().acquire() as conn:
            stmt_lyr = t_layer.insert().values(
                nome=fname
            ).returning(t_layer.c.id)

            row = await conn.execute(stmt_lyr)
            row = await row.fetchone()
            layer_id = row[0]

            stmt_prop = t_layer_properties.insert().values(
                layer_id=str(layer_id),
                propertie=json.dumps(feat['properties'])
            ).returning(t_layer_properties.c.id)

            row = await conn.execute(stmt_prop)
            row = await row.fetchone()
            property_id = row[0]

            geom = json.dumps(feat['geometry'])

            stmt_geom = t_layer_geometries.insert().values(
                layer_id=str(layer_id),
                propertie_id=str(property_id),
                geom=ST_SetSRID(ST_GeomFromGeoJSON(geom), 4674)
            )

            await conn.execute(stmt_geom)

