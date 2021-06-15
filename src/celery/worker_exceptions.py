#!-*-coding:utf-8-*-


class GeometryOutOfBrazil(Exception):

    def __init__(self):
        super(GeometryOutOfBrazil, self).__init__(
            'A geometria enviada está fora do território nacional.'
        )
