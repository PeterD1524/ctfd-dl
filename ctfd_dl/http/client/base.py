import abc
import contextlib

import ctfd_dl.http.exchanges
import ctfd_dl.http.requests


class Client(abc.ABC):
    @abc.abstractmethod
    def send(
        self, request: ctfd_dl.http.requests.Request
    ) -> contextlib.AbstractAsyncContextManager[ctfd_dl.http.exchanges.Exchange]:
        raise NotImplementedError
