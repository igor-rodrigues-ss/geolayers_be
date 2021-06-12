#!-*-coding:utf-8-*-


from src.apps.layer.mvt.operations.envelope import Envelope
from src.config import MERCATOR_SRID, MVT_DENSIFY_FACTOR


class EnvelopeSQL:

    _env: Envelope

    def __init__(self, layer_id: str, env: Envelope):
        self._env = env
        self._layer_id = layer_id

    def _bounds_sql(self):
        """
        Gera SQL para materializar um envelope de consulta em EPSG:3857.
        Densifique um pouco as bordas para que o envelope possa ser convertido
        com segurança em outros sistemas de coordenadas.
        """
        seg_size = (self._env.xmax() - self._env.xmin()) / MVT_DENSIFY_FACTOR
        return f"""
        ST_Segmentize(
            ST_MakeEnvelope(
                {self._env.xmin()}, {self._env.ymin()},
                {self._env.xmax()}, {self._env.ymax()},
                {MERCATOR_SRID}
            ),
            {seg_size}
        )
        """

    def sql(self):
        """Gere uma consulta SQL para extrair um bloco de dados MVT
        da tabela de interesse."""

        env_sql = self._bounds_sql()
        """
        Materializa os limites
        Selecione a geometria relevante e corte para os limites MVT
        Converta para o formato MVT
        """
        GEOM_COL = 'geom'
        SRID = 4674
        TABLE = 'layers.geometries'

        return f"""
            WITH 
            bounds AS (
                SELECT {env_sql} AS geom, 
                       {env_sql}::box2d AS b2d
            ),
            mvtgeom AS (
                SELECT ST_AsMVTGeom(
                    ST_Transform(t.{GEOM_COL}, {MERCATOR_SRID}),
                    bounds.b2d
                ) AS geom
                FROM {TABLE} t, bounds
                WHERE ST_Intersects(t.{GEOM_COL}, ST_Transform(bounds.geom, {SRID}))
                AND
                layer_id = '{self._layer_id}'
            ) 
            SELECT ST_AsMVT(mvtgeom.*) FROM mvtgeom
        """