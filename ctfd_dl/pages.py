from typing import TypedDict


class PageParams(TypedDict):
    page: int | None


def page_params(params: PageParams):
    page = params["page"]
    if page is None:
        return
    yield ("page", str(page))
