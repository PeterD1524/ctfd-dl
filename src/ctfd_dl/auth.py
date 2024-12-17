import dataclasses
import urllib.parse
from typing import TypedDict, override

import ctfd_dl.exceptions
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.resources
import ctfd_dl.type_adapters


@dataclasses.dataclass
class PostLoginParams(TypedDict):
    name: str
    password: str


@dataclasses.dataclass
class PostLogin(ctfd_dl.resources.Resource[PostLoginParams, None]):
    @override
    def request(self, params: PostLoginParams):
        return ctfd_dl.http.requests.Request(
            method="POST",
            url="/login",
            data=(("name", params["name"]), ("password", params["password"])),
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 302:
            headers = exchange.response.headers()
            location = headers.get("Location")
            if location != urllib.parse.urljoin(exchange.request.url, "/challenges"):
                raise ctfd_dl.exceptions.Error
        else:
            raise ctfd_dl.exceptions.Error


@dataclasses.dataclass
class Auth:
    post_login: PostLogin


def auth(type_adapter: ctfd_dl.type_adapters.TypeAdapter):
    return Auth(post_login=PostLogin(type_adapter))
