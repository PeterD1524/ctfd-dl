import abc
import dataclasses

import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.type_adapters


@dataclasses.dataclass
class Resource[P, R](abc.ABC):
    type_adapter: ctfd_dl.type_adapters.TypeAdapter

    @abc.abstractmethod
    def request(self, params: P) -> ctfd_dl.http.requests.Request:
        raise NotImplementedError

    @abc.abstractmethod
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange) -> R:
        raise NotImplementedError
