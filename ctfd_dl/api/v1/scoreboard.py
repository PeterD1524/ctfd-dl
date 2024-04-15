import dataclasses
from typing import TypedDict, override

import ctfd_dl.api.v1.schemas.core
import ctfd_dl.exceptions
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.namespaces
import ctfd_dl.resources


class GetScoreboardListParams(TypedDict):
    pass


@dataclasses.dataclass
class Member:
    id: int
    oauth_id: None  # int
    name: str
    score: int
    bracket_id: None  # int
    bracket_name: None  # str


@dataclasses.dataclass
class GetScoreboardListItemModel:
    pos: int
    account_id: int
    account_url: str
    account_type: str
    oauth_id: None  # int
    name: str
    score: int
    bracket_id: None  # int
    bracket_name: None  # str
    members: list[Member]


GetScoreboardListSuccessResponse = ctfd_dl.api.v1.schemas.core.APIListSuccessResponse[
    GetScoreboardListItemModel
]


# cached
class GetScoreboardList(
    ctfd_dl.resources.Resource[
        GetScoreboardListParams, GetScoreboardListSuccessResponse
    ]
):
    @override
    def request(self, params: GetScoreboardListParams):
        return ctfd_dl.http.requests.Request("GET", "")

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetScoreboardListSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetScoreboardDetailParams(TypedDict):
    count: int


@dataclasses.dataclass
class Solve:
    challenge_id: int
    account_id: int
    team_id: int
    user_id: int
    value: int
    date: str


@dataclasses.dataclass
class GetScoreboardDetailItemModel:
    id: int
    # account_url: str
    name: str
    # score: int
    # bracket_id: int
    # bracket_name: str
    solves: list[Solve]


GetScoreboardDetailSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.APIDetailedSuccessResponse[
        dict[str, GetScoreboardDetailItemModel]
    ]
)


# cached
class GetScoreboardDetail(
    ctfd_dl.resources.Resource[
        GetScoreboardDetailParams, GetScoreboardDetailSuccessResponse
    ]
):
    @override
    def request(self, params: GetScoreboardDetailParams):
        return ctfd_dl.http.requests.Request("GET", "/top/{}".format(params["count"]))

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetScoreboardDetailSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


@dataclasses.dataclass
class Scoreboard(ctfd_dl.namespaces.Namespace):
    get_scoreboard_list: GetScoreboardList
    get_scoreboard_detail: GetScoreboardDetail
