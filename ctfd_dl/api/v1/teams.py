import dataclasses
from typing import Literal, TypedDict, override

import ctfd_dl.api.v1.schemas.core
import ctfd_dl.exceptions
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.namespaces
import ctfd_dl.pages
import ctfd_dl.resources


class GetTeamListParams(ctfd_dl.pages.PageParams):
    pass


@dataclasses.dataclass
class GetTeamListItemModel:
    website: str | None
    name: str
    country: str | None
    affiliation: str | None
    bracket_id: None  # int
    id: int
    oauth_id: None  # int
    captain_id: int
    fields: tuple[()]


GetTeamListSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.PaginatedAPIListSuccessResponse[GetTeamListItemModel]
)


class GetTeamList(
    ctfd_dl.resources.Resource[GetTeamListParams, GetTeamListSuccessResponse]
):
    @override
    def request(self, params: GetTeamListParams):
        return ctfd_dl.http.requests.Request(
            "GET", "", params=tuple(ctfd_dl.pages.page_params(params))
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamListSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPublicParams(TypedDict):
    team_id: int


@dataclasses.dataclass
class GetTeamPublicModel:
    website: str | None
    name: str
    country: str | None
    affiliation: str | None
    bracket_id: None  # int
    members: list[int]
    id: int
    oauth_id: None  # int
    captain_id: int
    fields: tuple[()]
    place: str | None
    score: int


GetTeamPublicSuccessResponse = ctfd_dl.api.v1.schemas.core.APIDetailedSuccessResponse[
    GetTeamPublicModel
]


class GetTeamPublic(
    ctfd_dl.resources.Resource[GetTeamPublicParams, GetTeamPublicSuccessResponse]
):
    @override
    def request(self, params: GetTeamPublicParams):
        return ctfd_dl.http.requests.Request("GET", "/{}".format(params["team_id"]))

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPublicSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPrivateParams(TypedDict):
    pass


@dataclasses.dataclass
class GetTeamPrivateModel:
    website: str | None
    name: str
    email: str | None
    country: str | None
    affiliation: str | None
    bracket_id: None  # int
    members: list[int]
    id: int
    oauth_id: None  # int
    # password: str
    captain_id: int
    fields: tuple[()]
    place: str | None
    score: int


GetTeamPrivateSuccessResponse = ctfd_dl.api.v1.schemas.core.APIDetailedSuccessResponse[
    GetTeamPrivateModel
]


class GetTeamPrivate(
    ctfd_dl.resources.Resource[GetTeamPrivateParams, GetTeamPrivateSuccessResponse]
):
    @override
    def request(self, params: GetTeamPrivateParams):
        return ctfd_dl.http.requests.Request("GET", "/me")

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPrivateSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPrivateSolvesParams(TypedDict):
    pass


@dataclasses.dataclass
class Challenge:
    id: int
    name: str
    category: str
    value: int


@dataclasses.dataclass
class User:
    id: int
    name: str


@dataclasses.dataclass
class Team:
    id: int
    name: str


@dataclasses.dataclass
class Submission[T]:
    challenge_id: int
    challenge: Challenge
    user: User
    team: Team
    date: str
    type: T
    id: int


@dataclasses.dataclass
class Solve(Submission[Literal["correct"]]):
    type: Literal["correct"]


class GetTeamPrivateSolvesItemModel(Solve):
    pass


GetTeamPrivateSolvesSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.APIListSuccessResponseWithCountMeta[
        GetTeamPrivateSolvesItemModel
    ]
)


class GetTeamPrivateSolves(
    ctfd_dl.resources.Resource[
        GetTeamPrivateSolvesParams, GetTeamPrivateSolvesSuccessResponse
    ]
):
    @override
    def request(self, params: GetTeamPrivateSolvesParams):
        return ctfd_dl.http.requests.Request("GET", "/me/solves")

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPrivateSolvesSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPrivateFailsParams(TypedDict):
    pass


@dataclasses.dataclass
class Fail(Submission[Literal["incorrect"]]):
    type: Literal["incorrect"]


class GetTeamPrivateFailsItemModel(Fail):
    pass


GetTeamPrivateFailsSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.APIListSuccessResponseWithCountMeta[
        GetTeamPrivateFailsItemModel
    ]
)


class GetTeamPrivateFails(
    ctfd_dl.resources.Resource[
        GetTeamPrivateFailsParams, GetTeamPrivateFailsSuccessResponse
    ]
):
    @override
    def request(self, params: GetTeamPrivateFailsParams):
        return ctfd_dl.http.requests.Request("GET", "/me/fails")

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPrivateFailsSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPrivateAwardsParams(TypedDict):
    pass


@dataclasses.dataclass
class GetTeamPrivateAwardsItemModel:
    pass


GetTeamPrivateAwardsSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.APIListSuccessResponseWithCountMeta[
        GetTeamPrivateAwardsItemModel
    ]
)


class GetTeamPrivateAwards(
    ctfd_dl.resources.Resource[
        GetTeamPrivateAwardsParams, GetTeamPrivateAwardsSuccessResponse
    ]
):
    @override
    def request(self, params: GetTeamPrivateAwardsParams):
        return ctfd_dl.http.requests.Request("GET", "/me/awards")

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPrivateAwardsSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPublicSolvesParams(TypedDict):
    team_id: int


class GetTeamPublicSolvesItemModel(Solve):
    pass


GetTeamPublicSolvesSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.APIListSuccessResponseWithCountMeta[
        GetTeamPublicSolvesItemModel
    ]
)


class GetTeamPublicSolves(
    ctfd_dl.resources.Resource[
        GetTeamPublicSolvesParams, GetTeamPublicSolvesSuccessResponse
    ]
):
    @override
    def request(self, params: GetTeamPublicSolvesParams):
        return ctfd_dl.http.requests.Request(
            "GET", "/{}/solves".format(params["team_id"])
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPublicSolvesSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPublicFailsParams(TypedDict):
    team_id: int


class GetTeamPublicFailsItemModel(Fail):
    pass


GetTeamPublicFailsSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.APIListSuccessResponseWithCountMeta[
        GetTeamPublicFailsItemModel
    ]
)


class GetTeamPublicFails(
    ctfd_dl.resources.Resource[
        GetTeamPublicFailsParams, GetTeamPublicFailsSuccessResponse
    ]
):
    @override
    def request(self, params: GetTeamPublicFailsParams):
        return ctfd_dl.http.requests.Request(
            "GET", "/{}/fails".format(params["team_id"])
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPublicFailsSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetTeamPublicAwardsParams(TypedDict):
    team_id: int


@dataclasses.dataclass
class GetTeamPublicAwardsItemModel:
    pass


GetTeamPublicAwardsSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.APIListSuccessResponseWithCountMeta[
        GetTeamPublicAwardsItemModel
    ]
)


class GetTeamPublicAwards(
    ctfd_dl.resources.Resource[
        GetTeamPublicAwardsParams, GetTeamPublicAwardsSuccessResponse
    ]
):
    @override
    def request(self, params: GetTeamPublicAwardsParams):
        return ctfd_dl.http.requests.Request(
            "GET", "/{}/awards".format(params["team_id"])
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetTeamPublicAwardsSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


@dataclasses.dataclass
class Teams(ctfd_dl.namespaces.Namespace):
    get_team_list: GetTeamList
    get_team_public: GetTeamPublic
    get_team_private: GetTeamPrivate
    get_team_private_solves: GetTeamPrivateSolves
    get_team_private_fails: GetTeamPrivateFails
    get_team_private_awards: GetTeamPrivateAwards
    get_team_public_solves: GetTeamPublicSolves
    get_team_public_fails: GetTeamPublicFails
    get_team_public_awards: GetTeamPublicAwards
