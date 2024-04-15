import dataclasses

import ctfd_dl.http.requests


@dataclasses.dataclass
class Namespace:
    path: str

    def request(self, request: ctfd_dl.http.requests.Request):
        request = ctfd_dl.http.requests.copy(request)
        request.url = self.path + request.url
        return request
