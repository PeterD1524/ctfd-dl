import contextlib
import dataclasses
from typing import override

import httpx

import ctfd_dl.exceptions
import ctfd_dl.http.client.base
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.http.response.httpx


@dataclasses.dataclass
class Client(ctfd_dl.http.client.base.Client):
    client: httpx.AsyncClient

    @override
    @contextlib.asynccontextmanager
    async def send(self, request: ctfd_dl.http.requests.Request):
        data = request.data
        if data is not None:
            length = len(data)
            data = dict(data)
            if len(data) != length:
                raise ctfd_dl.exceptions.Error
        async with self.client.stream(
            request.method,
            request.url,
            data=data,
            params=ctfd_dl.http.requests.copy_iterable(request.params),
            follow_redirects=request.follow_redirects,
        ) as response:
            yield ctfd_dl.http.exchanges.Exchange(
                request=request,
                response=ctfd_dl.http.response.httpx.Response(response=response),
            )


@contextlib.asynccontextmanager
async def client():
    async with httpx.AsyncClient(timeout=None) as client:
        yield Client(client)
