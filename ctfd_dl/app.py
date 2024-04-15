import dataclasses
import urllib.parse

import ctfd_dl.api.core
import ctfd_dl.auth
import ctfd_dl.http.requests
import ctfd_dl.type_adapters
import ctfd_dl.views


@dataclasses.dataclass
class BaseUrl:
    base: str

    def request(self, request: ctfd_dl.http.requests.Request):
        request = ctfd_dl.http.requests.copy(request)
        request.url = urllib.parse.urljoin(self.base, request.url)
        return request


@dataclasses.dataclass
class App:
    base_url: BaseUrl

    views: ctfd_dl.views.Views
    auth: ctfd_dl.auth.Auth
    api: ctfd_dl.api.core.ApiV1


def app(base_url: str, type_adapter: ctfd_dl.type_adapters.TypeAdapter):
    return App(
        base_url=BaseUrl(base=base_url),
        views=ctfd_dl.views.views(type_adapter),
        auth=ctfd_dl.auth.auth(type_adapter),
        api=ctfd_dl.api.core.api_v1(type_adapter),
    )
