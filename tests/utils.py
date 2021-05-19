#!-*-coding:utf-8-*-


from uuid import UUID


def is_uuid(val: str):
    try:
        _ = UUID(val, version=4)
    except ValueError:
        return False
    return True