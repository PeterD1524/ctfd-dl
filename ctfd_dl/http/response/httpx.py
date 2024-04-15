import dataclasses
from typing import override

import httpx

import ctfd_dl.http.headers.httpx
import ctfd_dl.http.requests
import ctfd_dl.http.response.base


@dataclasses.dataclass
class Response(ctfd_dl.http.response.base.Response):
    response: httpx.Response

    @override
    def status_code(self):
        return self.response.status_code

    @override
    async def read(self):
        return await self.response.aread()

    @override
    def headers(self):
        return ctfd_dl.http.headers.httpx.Headers(self.response.headers)

    @override
    async def text(self):
        await self.response.aread()
        return self.response.text
