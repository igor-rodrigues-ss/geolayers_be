#!-*-coding:utf-8-*-



from src.apps.layer.mvt.tile import Tile


class Envelope:

    def __init__(self, tile: Tile):
        self._tile = tile

        # Largura do mundo em EPSG:3857
        self._world_merc_max = 20037508.3427892
        self._world_merc_min = -1 * self._world_merc_max

        world_merc_size = self._world_merc_max - self._world_merc_min
        
        # largura dos tiles
        world_tile_size = 2 ** tile.zoom()
        
        # Largura dos tiles em EPSG:3857
        self._tile_merc_size = world_merc_size / world_tile_size


    # Calculate geographic bounds from tile coordinates
    # XYZ tile coordinates are in "image space" so origin is
    # top-left, not bottom right

    def xmin(self):
        return self._world_merc_min + self._tile_merc_size * self._tile.x()

    def xmax(self):
        return self._world_merc_min + self._tile_merc_size * (self._tile.x() + 1)

    def ymin(self):
        return self._world_merc_max - self._tile_merc_size * (self._tile.y() + 1)

    def ymax(self):
        return self._world_merc_max - self._tile_merc_size * self._tile.y()
