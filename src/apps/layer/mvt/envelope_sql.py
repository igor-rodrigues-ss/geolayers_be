#!-*-coding:utf-8-*-




from src.apps.layer.mvt.envelope import Envelope
# from src.config upload MERCATOR_SRID, MVT_DENSIFY_FACTOR

MERCATOR_SRID = 3857
MVT_DENSIFY_FACTOR = 4

class EnvelopeSQL:

    _env: Envelope

    def __init__(self, env: Envelope, mvt_lyr_data: dict):
        self._env = env
        self._mvt_lyr_data = mvt_lyr_data

    def _bounds_sql(self):
        """
        Gere SQL para materializar um envelope de consulta em EPSG: 3857.
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
        geom_col = 'geom'
        attr_cols = 'id'
        srid_lyr = 4674
        table = 'layer_geometries'

        return f"""
            WITH 
            bounds AS (
                SELECT {env_sql} AS geom, 
                       {env_sql}::box2d AS b2d
            ),
            mvtgeom AS (
                SELECT ST_AsMVTGeom(
                    ST_Transform(t.{geom_col}, {MERCATOR_SRID}),
                    bounds.b2d
                ) AS geom,
                {attr_cols}
                FROM {table} t, bounds
                WHERE ST_Intersects(t.{geom_col}, ST_Transform(bounds.geom, {srid_lyr}))
            ) 
            SELECT ST_AsMVT(mvtgeom.*) FROM mvtgeom
        """