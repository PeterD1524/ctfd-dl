import dataclasses
from typing import Literal


@dataclasses.dataclass
class APISimpleSuccessResponse:
    success: Literal[True]


@dataclasses.dataclass
class APIDetailedSuccessResponse[T](APISimpleSuccessResponse):
    data: T


# this does not work with pydantic
# https://docs.python.org/3/library/types.html#types.get_original_bases
# https://peps.python.org/pep-0560/
#
# https://github.com/pydantic/pydantic/issues/7479
# class APIListSuccessResponse[T](APIDetailedSuccessResponse[list[T]]):
#     pass

# does not work with pyright
# type APIListSuccessResponse[T] = APIDetailedSuccessResponse[list[T]]

# workaround 1
# T = TypeVar("T")
# APIListSuccessResponse = APIDetailedSuccessResponse[list[T]]


# workaround 2
# explicit override
@dataclasses.dataclass
class APIListSuccessResponse[T](APIDetailedSuccessResponse[list[T]]):
    data: list[T]


@dataclasses.dataclass
class WithMeta[T]:
    meta: T


@dataclasses.dataclass
class CountMeta:
    count: int


@dataclasses.dataclass
class APIListSuccessResponseWithCountMeta[T](
    APIDetailedSuccessResponse[list[T]], WithMeta[CountMeta]
):
    data: list[T]
    meta: CountMeta


@dataclasses.dataclass
class Pagination:
    page: int
    next: int | None
    prev: int | None
    pages: int
    per_page: int
    total: int


@dataclasses.dataclass
class PaginationMeta:
    pagination: Pagination


@dataclasses.dataclass
class PaginatedAPIListSuccessResponse[T](
    APIListSuccessResponse[T], WithMeta[PaginationMeta]
):
    data: list[T]
    meta: PaginationMeta


@dataclasses.dataclass
class APISimpleErrorResponse:
    success: Literal[False]
    errors: list[str] | None
