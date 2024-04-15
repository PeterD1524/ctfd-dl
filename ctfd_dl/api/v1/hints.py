import dataclasses
from typing import TypedDict, override

import ctfd_dl.api.v1.schemas.core
import ctfd_dl.exceptions
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.namespaces
import ctfd_dl.resources


class GetHintParams(TypedDict):
    hint_id: int


@dataclasses.dataclass
class GetHintModel:
    id: int
    type: str
    challenge: int
    challenge_id: int
    content: str
    html: str
    cost: int


GetHintSuccessResponse = ctfd_dl.api.v1.schemas.core.APIDetailedSuccessResponse[
    GetHintModel
]


class GetHint(ctfd_dl.resources.Resource[GetHintParams, GetHintSuccessResponse]):
    @override
    def request(self, params: GetHintParams):
        return ctfd_dl.http.requests.Request("GET", "/{}".format(params["hint_id"]))

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetHintSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


@dataclasses.dataclass
class Hints(ctfd_dl.namespaces.Namespace):
    get_hint: GetHint
