import dataclasses

import ctfd_dl.http.requests
import ctfd_dl.http.response.base


@dataclasses.dataclass
class Exchange:
    request: ctfd_dl.http.requests.Request
    response: ctfd_dl.http.response.base.Response
