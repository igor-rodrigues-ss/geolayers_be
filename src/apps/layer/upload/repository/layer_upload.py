#!-*-coding:utf-8-*-


import json
from typing import Generator
from sqlalchemy.engine.base import Connection
from geoalchemy2.functions import ST_GeomFromGeoJSON, ST_SetSRID
from src.db.models import t_styles, t_layer, t_geometries, t_properties
from uuid import UUID


class LayerUploadRepository:

    _features: Generator[str, None, None]
    _conn: Connection
    _lyr_name: str
    _color: str
    _fill: bool

    def __init__(
        self, conn: Connection, lyr_name: str, features: Generator[str, None, None],
        color: str, fill: bool
    ):
        self._conn = conn
        self._features = features
        self._lyr_name = lyr_name
        self._color = color
        self._fill = fill

    def _save_style(self, layer_id: UUID):
        stmt = t_styles.insert().values(
            layer_id=layer_id,
            color=self._color,
            fill=self._fill
        )
        self._conn.execute(stmt)

    def _save_layer(self) -> UUID:
        stmt_lyr = t_layer.insert().values(
            nome=self._lyr_name
        ).returning(t_layer.c.id)

        row = self._conn.execute(stmt_lyr)
        row = row.fetchone()
        return row[0]

    def _save_properties(self, layer_id: UUID, feat) -> UUID:
        stmt_prop = t_properties.insert().values(
            layer_id=str(layer_id),
            properties=json.dumps(feat['properties'])
        ).returning(t_properties.c.id)

        row = self._conn.execute(stmt_prop)
        row = row.fetchone()
        return row[0]

    def _save_geometry(self, layer_id: UUID, property_id: UUID, feat):
        geom = json.dumps(feat['geometry'])
        stmt_geom = t_geometries.insert().values(
            layer_id=str(layer_id),
            properties_id=str(property_id),
            geom=ST_SetSRID(ST_GeomFromGeoJSON(geom), 4674)
        )
        self._conn.execute(stmt_geom)

    def save(self):
        with self._conn.begin():
            layer_id = self._save_layer()
            self._save_style(layer_id)

            for feat in self._features:
                feat = json.loads(feat)
                property_id = self._save_properties(layer_id, feat)
                self._save_geometry(layer_id, property_id, feat)
