#!-*-coding:utf-8-*-

import json
import pytest
from fastapi import status
from src.middlewares.try_except import try_except
from src.framework.exc_codes import UNEXPECTED_ERROR


EXC = Exception('Error ABC')


def call_next_mock(request):
    raise EXC


class TestMiddlewareTryExcept:

    @pytest.mark.asyncio
    async def test_unexpected_error_status_500(self):
        resp = await try_except(None, call_next_mock)
        assert resp.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

    @pytest.mark.asyncio
    async def test_unexpected_error_code(self):
        resp = await try_except(None, call_next_mock)
        resp_data = json.loads(resp.body.decode('utf-8'))
        assert resp_data['detail']['code'] == UNEXPECTED_ERROR

    @pytest.mark.asyncio
    async def test_unexpected_error_msg(self):
        resp = await try_except(None, call_next_mock)
        resp_data = json.loads(resp.body.decode('utf-8'))
        assert bool(resp_data['detail']['msg'])

    @pytest.mark.asyncio
    async def test_unexpected_error_exc(self):
        resp = await try_except(None, call_next_mock)
        resp_data = json.loads(resp.body.decode('utf-8'))
        exc = f'{EXC.__class__.__name__}: {str(EXC)}'
        assert resp_data['detail']['exc'] == exc
