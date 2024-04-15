import dataclasses
from typing import TypedDict, override

import ctfd_dl.exceptions
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.resources
import ctfd_dl.type_adapters


class GetStaticHtmlParams(TypedDict):
    route: str


class GetStaticHtml(ctfd_dl.resources.Resource[GetStaticHtmlParams, str]):
    @override
    def request(self, params: GetStaticHtmlParams):
        return ctfd_dl.http.requests.Request(
            method="GET", url="/{}".format(params["route"])
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            if (
                exchange.response.headers().get("Content-Type")
                != "text/html; charset=utf-8"
            ):
                raise ctfd_dl.exceptions.Error
            return await exchange.response.text()
        else:
            raise ctfd_dl.exceptions.Error


class GetFilesParams(TypedDict):
    path: str | None
    token: str | None


class GetFiles(ctfd_dl.resources.Resource[GetFilesParams, bytes]):
    @override
    def request(self, params: GetFilesParams):
        path = params["path"]
        return ctfd_dl.http.requests.Request(
            method="GET",
            url="/files" if path is None else "/files/{}".format(path),
            follow_redirects=True,
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return await exchange.response.read()
        else:
            raise ctfd_dl.exceptions.Error


@dataclasses.dataclass
class Views:
    get_static_html: GetStaticHtml
    get_files: GetFiles


def views(type_adapter: ctfd_dl.type_adapters.TypeAdapter):
    return Views(
        get_static_html=GetStaticHtml(type_adapter), get_files=GetFiles(type_adapter)
    )
