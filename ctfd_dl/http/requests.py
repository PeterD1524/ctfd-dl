import dataclasses
import itertools
from collections.abc import Iterable, Sequence


@dataclasses.dataclass
class Request:
    method: str
    url: str
    data: Sequence[tuple[str, str]] | None = None
    params: Sequence[tuple[str, str]] | None = None
    follow_redirects: bool = False


def copy_iterable[T](iterable: Iterable[T] | None):
    if iterable is None:
        return None
    return tuple(iterable)


def copy(request: Request):
    return Request(
        method=request.method,
        url=request.url,
        data=copy_iterable(request.data),
        params=copy_iterable(request.params),
        follow_redirects=request.follow_redirects,
    )


def merge_iterable(a: Iterable[tuple[str, str]] | None, b: Iterable[tuple[str, str]]):
    if a is None:
        return tuple(b)
    return tuple(itertools.chain(a, b))
