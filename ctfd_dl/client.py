import contextlib
import dataclasses

import ctfd_dl.app
import ctfd_dl.exceptions
import ctfd_dl.html
import ctfd_dl.http.client.base
import ctfd_dl.http.exchanges
import ctfd_dl.http.requests
import ctfd_dl.requests


@dataclasses.dataclass
class Result[T]:
    exchange: ctfd_dl.http.exchanges.Exchange
    value: T


def add_nonce_to_form(request: ctfd_dl.http.requests.Request, nonce: str):
    request.data = ctfd_dl.http.requests.merge_iterable(
        request.data, (("nonce", nonce),)
    )


def login_get_nonce(document: ctfd_dl.html.HtmlElement):
    (input,) = document.xpath('//*[@id="nonce"]')
    if not isinstance(input, ctfd_dl.html.InputElement):
        raise ctfd_dl.exceptions.Error
    value = input.get("value")
    return value


@dataclasses.dataclass
class Client:
    app: ctfd_dl.app.App
    http: ctfd_dl.http.client.base.Client
    requests: ctfd_dl.requests.Requests

    async def login(self, *, name: str, password: str):
        request = self.app.base_url.request(
            self.app.views.get_static_html.request({"route": "login"})
        )
        async with self.http.send(request) as exchange:
            text = await self.app.views.get_static_html.response(exchange)
        document = ctfd_dl.html.document_from_string(text)
        nonce = login_get_nonce(document)
        request = self.app.auth.post_login.request({"name": name, "password": password})
        add_nonce_to_form(request, nonce)
        request = self.app.base_url.request(request)
        async with self.http.send(request) as exchange:
            await self.app.auth.post_login.response(exchange)

    @contextlib.asynccontextmanager
    async def get_challenge_list(self):
        request = self.requests.get_challenge_list({})
        async with self.http.send(request) as exchange:
            value = await self.app.api.challenges.get_challenge_list.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_challenge(self, *, challenge_id: int):
        request = self.requests.get_challenge({"challenge_id": challenge_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.challenges.get_challenge.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_challenge_solves(self, *, challenge_id: int):
        request = self.requests.get_challenge_solves({"challenge_id": challenge_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.challenges.get_challenge_solves.response(
                exchange
            )
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_hint(self, *, hint_id: int):
        request = self.requests.get_hint({"hint_id": hint_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.hints.get_hint.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_scoreboard_list(self):
        request = self.requests.get_scoreboard_list({})
        async with self.http.send(request) as exchange:
            value = await self.app.api.scoreboard.get_scoreboard_list.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_scoreboard_detail(self, *, count: int):
        request = self.requests.get_scoreboard_detail({"count": count})
        async with self.http.send(request) as exchange:
            value = await self.app.api.scoreboard.get_scoreboard_detail.response(
                exchange
            )
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_list(self, *, page: int | None = None):
        request = self.requests.get_team_list({"page": page})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_list.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_public(self, *, team_id: int):
        request = self.requests.get_team_public({"team_id": team_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_public.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_private(self):
        request = self.requests.get_team_private({})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_private.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_private_solves(self):
        request = self.requests.get_team_private_solves({})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_private_solves.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_private_fails(self):
        request = self.requests.get_team_private_fails({})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_private_fails.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_private_awards(self):
        request = self.requests.get_team_private_fails_awards({})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_private_awards.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_public_solves(self, *, team_id: int):
        request = self.requests.get_team_public_solves({"team_id": team_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_public_solves.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_public_fails(self, *, team_id: int):
        request = self.requests.get_team_public_fails({"team_id": team_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_public_fails.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_team_public_awards(self, *, team_id: int):
        request = self.requests.get_team_public_awards({"team_id": team_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.teams.get_team_public_awards.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_user_list(self, *, page: int | None = None):
        request = self.requests.get_user_list({"page": page})
        async with self.http.send(request) as exchange:
            value = await self.app.api.users.get_user_list.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_user_public(self, *, user_id: int):
        request = self.requests.get_user_public({"user_id": user_id})
        async with self.http.send(request) as exchange:
            value = await self.app.api.users.get_user_public.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_user_private(self):
        request = self.requests.get_user_private({})
        async with self.http.send(request) as exchange:
            value = await self.app.api.users.get_user_private.response(exchange)
            yield Result(exchange=exchange, value=value)

    @contextlib.asynccontextmanager
    async def get_files(self, *, path: str | None, token: str | None):
        request = self.app.base_url.request(
            self.app.views.get_files.request({"path": path, "token": token})
        )
        async with self.http.send(request) as exchange:
            yield Result(
                exchange=exchange,
                value=await self.app.views.get_files.response(exchange),
            )
