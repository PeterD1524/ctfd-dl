import dataclasses
from typing import TypedDict, override

import ctfd_dl.api.v1.schemas.core
import ctfd_dl.exceptions
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.namespaces
import ctfd_dl.pages
import ctfd_dl.resources


class GetUserListParams(ctfd_dl.pages.PageParams):
    pass


@dataclasses.dataclass
class GetUserListItemModel:
    website: str | None
    name: str
    country: str | None
    affiliation: str | None
    bracket_id: None  # int
    id: int
    oauth_id: None  # int
    fields: tuple[()]
    team_id: int | None


GetUserListSuccessResponse = (
    ctfd_dl.api.v1.schemas.core.PaginatedAPIListSuccessResponse[GetUserListItemModel]
)


class GetUserList(
    ctfd_dl.resources.Resource[GetUserListParams, GetUserListSuccessResponse]
):
    @override
    def request(self, params: GetUserListParams):
        return ctfd_dl.http.requests.Request(
            "GET", "", params=tuple(ctfd_dl.pages.page_params(params))
        )

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetUserListSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetUserPublicParams(TypedDict):
    user_id: int


@dataclasses.dataclass
class GetUserPublicModel:
    website: str | None
    name: str
    country: str | None
    affiliation: str | None
    bracket_id: None  # int
    id: int
    oauth_id: None  # int
    fields: tuple[()]
    team_id: int | None


GetUserPublicSuccessResponse = ctfd_dl.api.v1.schemas.core.APIDetailedSuccessResponse[
    GetUserPublicModel
]


class GetUserPublic(
    ctfd_dl.resources.Resource[GetUserPublicParams, GetUserPublicSuccessResponse]
):
    @override
    def request(self, params: GetUserPublicParams):
        return ctfd_dl.http.requests.Request("GET", "/{}".format(params["user_id"]))

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetUserPublicSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


class GetUserPrivateParams(TypedDict):
    pass


@dataclasses.dataclass
class GetUserPrivateModel:
    website: str | None
    name: str
    email: str
    language: str | None
    country: str | None
    affiliation: str | None
    bracket_id: None  # int
    id: int
    oauth_id: None  # int
    fields: tuple[()]
    team_id: int | None
    place: str | None
    score: int


GetUserPrivateSuccessResponse = ctfd_dl.api.v1.schemas.core.APIDetailedSuccessResponse[
    GetUserPrivateModel
]


class GetUserPrivate(
    ctfd_dl.resources.Resource[GetUserPrivateParams, GetUserPrivateSuccessResponse]
):
    @override
    def request(self, params: GetUserPrivateParams):
        return ctfd_dl.http.requests.Request("GET", "/me")

    @override
    async def response(self, exchange: ctfd_dl.http.exchanges.Exchange):
        if exchange.response.status_code() == 200:
            return self.type_adapter.validate_json(
                GetUserPrivateSuccessResponse, await exchange.response.read()
            )
        else:
            raise ctfd_dl.exceptions.Error


@dataclasses.dataclass
class Users(ctfd_dl.namespaces.Namespace):
    get_user_list: GetUserList
    get_user_public: GetUserPublic
    get_user_private: GetUserPrivate
