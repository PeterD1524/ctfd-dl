import dataclasses
from typing import override

import httpx

import ctfd_dl.http.headers.base


@dataclasses.dataclass
class Headers(ctfd_dl.http.headers.base.Headers):
    headers: httpx.Headers

    @override
    def get(self, key: str):
        return self.headers[key]
