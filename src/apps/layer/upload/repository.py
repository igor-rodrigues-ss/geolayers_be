#!-*-coding:utf-8-*-

import json
from src.db.default_connection import DB_DEFAULT
from geoalchemy2.functions import ST_GeomFromGeoJSON, ST_SetSRID
from src.models import *
from uuid import UUID


class LayerImportRepo:

    _features = None
    _lyr_name = None

    def __init__(self, lyr_name, features):
        self._features = features
        self._lyr_name = lyr_name

    async def _save_layer(self, conn) -> UUID:
        stmt_lyr = t_layer.insert().values(
            nome=self._lyr_name
        ).returning(t_layer.c.id)

        row = await conn.execute(stmt_lyr)
        row = await row.fetchone()
        return row[0]

    async def _save_properties(self, conn, layer_id: UUID, feat) -> UUID:
        stmt_prop = t_layer_properties.insert().values(
            layer_id=str(layer_id),
            propertie=json.dumps(feat['properties'])
        ).returning(t_layer_properties.c.id)

        row = await conn.execute(stmt_prop)
        row = await row.fetchone()
        return row[0]

    async def _save_geometry(self, conn, layer_id: UUID, property_id: UUID, feat):
        geom = json.dumps(feat['geometry'])
        stmt_geom = t_layer_geometries.insert().values(
            layer_id=str(layer_id),
            propertie_id=str(property_id),
            geom=ST_SetSRID(ST_GeomFromGeoJSON(geom), 4674)
        )
        await conn.execute(stmt_geom)

    async def save(self):
        # TODO: criar transação
        print('Inserindo camada......')
        async with DB_DEFAULT.pool().acquire() as conn:
            layer_id = await self._save_layer(conn)
            for feat in self._features:
                feat = json.loads(feat)
                property_id = await self._save_properties(conn, layer_id, feat)
                await self._save_geometry(conn, layer_id, property_id, feat)