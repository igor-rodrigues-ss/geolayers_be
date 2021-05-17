#!-*-coding:utf-8-*-


import json
from src.db.default_conn_celery import engine
from geoalchemy2.functions import ST_GeomFromGeoJSON, ST_SetSRID
from src.models import *
from uuid import UUID


class LayerImportRepo:

    _features = None
    _lyr_name = None

    def __init__(self, lyr_name, features, color: str, fill: bool):
        self._features = features
        self._lyr_name = lyr_name
        self._color = color
        self._fill = fill

    def _save_style(self, layer_id: UUID, conn):
        stmt = t_styles.insert().values(
            id_layer=layer_id,
            color=self._color,
            fill=self._fill
        )
        conn.execute(stmt)

    def _save_layer(self, conn) -> UUID:
        stmt_lyr = t_layer.insert().values(
            nome=self._lyr_name
        ).returning(t_layer.c.id)

        row = conn.execute(stmt_lyr)
        row = row.fetchone()
        return row[0]

    def _save_properties(self, conn, layer_id: UUID, feat) -> UUID:
        stmt_prop = t_layer_properties.insert().values(
            layer_id=str(layer_id),
            propertie=json.dumps(feat['properties'])
        ).returning(t_layer_properties.c.id)

        row = conn.execute(stmt_prop)
        row = row.fetchone()
        return row[0]

    def _save_geometry(self, conn, layer_id: UUID, property_id: UUID, feat):
        geom = json.dumps(feat['geometry'])
        stmt_geom = t_layer_geometries.insert().values(
            layer_id=str(layer_id),
            propertie_id=str(property_id),
            geom=ST_SetSRID(ST_GeomFromGeoJSON(geom), 4674)
        )
        conn.execute(stmt_geom)

    def _save(self, conn):
        # TODO: criar transação
        print('Inserindo camada......')

        layer_id = self._save_layer(conn)
        self._save_style(layer_id, conn)

        for feat in self._features:
            feat = json.loads(feat)
            property_id = self._save_properties(conn, layer_id, feat)
            self._save_geometry(conn, layer_id, property_id, feat)

    def save(self, task_id: str):
        PENDING = 'PENDING'
        SUCCESS = 'SUCCESS'
        FAILURE = 'FAILURE'

        with engine.connect() as conn:
            try:
                conn.execute(
                    t_save_layer.insert().values(
                        id=task_id, status=PENDING, layer_name=self._lyr_name
                    )
                )
                self._save(conn)
            except Exception as exc:
                conn.execute(
                    t_save_layer.update().values(status=FAILURE, detail=str(exc)).where(
                        t_save_layer.c.id == task_id
                    )
                )
            else:
                conn.execute(
                    t_save_layer.update().values(status=SUCCESS, detail='').where(
                        t_save_layer.c.id == task_id
                    )
                )
