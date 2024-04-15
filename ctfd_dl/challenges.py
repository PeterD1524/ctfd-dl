import urllib.parse

import ctfd_dl.exceptions
import ctfd_dl.views


def challenge_file_url_to_params(url: str):
    result = urllib.parse.urlparse(url)
    if not (
        result.scheme == ""
        and result.netloc == ""
        and result.path.startswith("/files")
        and result.params == ""
        and result.fragment == ""
    ):
        raise ctfd_dl.exceptions.Error
    path = result.path[len("/files") :]
    if path.startswith("/"):
        path = path[len("/") :]
    else:
        path = None
    query = urllib.parse.parse_qsl(result.query)
    if len(query) != 1:
        raise ctfd_dl.exceptions.Error
    name, value = query[0]
    if name != "token":
        raise ctfd_dl.exceptions.Error
    return ctfd_dl.views.GetFilesParams(path=path, token=value)
