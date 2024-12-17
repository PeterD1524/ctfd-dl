import abc

import ctfd_dl.http.headers.base
import ctfd_dl.http.requests


class Response(abc.ABC):
    @abc.abstractmethod
    def status_code(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    async def read(self) -> bytes:
        raise NotImplementedError

    @abc.abstractmethod
    def headers(self) -> ctfd_dl.http.headers.base.Headers:
        raise NotImplementedError

    @abc.abstractmethod
    async def text(self) -> str:
        raise NotImplementedError
