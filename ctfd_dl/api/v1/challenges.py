import dataclasses
from typing import TypedDict, override

import ctfd_dl.api.v1.schemas.core
import ctfd_dl.exceptions
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.namespaces
import ctfd_dl.plugins.challenges.core
import ctfd_dl.resources


class GetChallengeListParams(TypedDict):
    pass


@dataclasses.dataclass
class Tag:
    value: str


@dataclasses.dataclass
class GetChallengeListItemModel:
    id: int
    type: str
    name: str
    value: int
    solves: int
    solved_by_me: bool
    category: str
    tags: list[Tag]
    template: str
    script: str


GetChallengeListSuccessResponse = ctfd_dl.api.v1.schemas.core.APIListSuccessResponse[
    GetChallengeListItemModel
]


class GetChallengeList(
    ctfd_dl.resources.Resource[GetChallengeListParams, GetChallengeListSuccessResponse]
):
    @override
    def request(self, params: GetChallengeListParams):
        return ctfd_dl.http.requests.Request(method="GET", url="")

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetChallengeListSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetChallengeParams(TypedDict):
    challenge_id: int


@dataclasses.dataclass
class Hint:
    id: int
    cost: int


@dataclasses.dataclass
class GetChallengeModel:
    solves: int
    solved_by_me: bool
    attempts: int
    files: list[str]
    tags: list[str]
    hints: list[Hint]
    view: str


GetChallengeSuccessResponse = ctfd_dl.api.v1.schemas.core.APIDetailedSuccessResponse[
    GetChallengeModel
]


class GetChallenge(
    ctfd_dl.resources.Resource[GetChallengeParams, GetChallengeSuccessResponse]
):
    @override
    def request(self, params: GetChallengeParams):
        return ctfd_dl.http.requests.Request(
            "GET", "/{}".format(params["challenge_id"])
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetChallengeSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetChallengeSolvesParams(TypedDict):
    challenge_id: int


@dataclasses.dataclass
class GetChallengeSolvesItemModel:
    account_id: int
    name: str
    date: str
    account_url: str


GetChallengeSolvesSuccessResponse = ctfd_dl.api.v1.schemas.core.APIListSuccessResponse[
    GetChallengeSolvesItemModel
]


class GetChallengeSolves(
    ctfd_dl.resources.Resource[
        GetChallengeSolvesParams, GetChallengeSolvesSuccessResponse
    ]
):
    @override
    def request(self, params: GetChallengeSolvesParams):
        return ctfd_dl.http.requests.Request(
            "GET", "/{}/solves".format(params["challenge_id"])
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetChallengeSolvesSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


@dataclasses.dataclass
class Challenges(ctfd_dl.namespaces.Namespace):
    get_challenge_list: GetChallengeList
    get_challenge: GetChallenge
    get_challenge_solves: GetChallengeSolves
