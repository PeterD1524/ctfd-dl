import contextlib
import dataclasses
import pathlib
import urllib.parse
from collections.abc import Iterable

import ctfd_dl.app
import ctfd_dl.challenges
import ctfd_dl.client
import ctfd_dl.exceptions
import ctfd_dl.http.client.httpx
import ctfd_dl.http.exchanges
import ctfd_dl.requests
import ctfd_dl.type_adapters


@contextlib.asynccontextmanager
async def client(base_url: str):
    app = ctfd_dl.app.app(
        base_url=base_url, type_adapter=ctfd_dl.type_adapters.type_adapter()
    )
    async with ctfd_dl.http.client.httpx.client() as http:
        yield ctfd_dl.client.Client(
            app=app, http=http, requests=ctfd_dl.requests.Requests(app)
        )


@dataclasses.dataclass
class Downloader:
    client: ctfd_dl.client.Client
    directory: pathlib.Path

    async def download(self):
        await self.download_challenge_list()
        # await self.download_scoreboard()
        # await self.download_team_list()
        # await self.download_team_private()
        # await self.download_user_list()
        # await self.download_user_private()
        pass

    async def download_challenge_list(self):
        async with self.client.get_challenge_list() as result:
            await self.write_json(result.exchange)
        for challenge in result.value.data:
            await self.download_challenge(challenge_id=challenge.id)
            # async with self.client.get_challenge_solves(
            #     challenge_id=challenge.id
            # ) as result:
            #     await self.write_json(result.exchange)

    async def download_challenge(self, *, challenge_id: int):
        async with self.client.get_challenge(challenge_id=challenge_id) as result:
            print(result.value.data.files)
            await self.write_json(result.exchange)
            for file in result.value.data.files:
                await self.download_challenge_file(file)
        for hint in result.value.data.hints:
            async with self.client.get_hint(hint_id=hint.id) as result:
                await self.write_json(result.exchange)

    async def download_scoreboard_list(self):
        async with self.client.get_scoreboard_list() as result:
            await self.write_json(result.exchange)
            async with self.client.get_scoreboard_detail(
                count=len(result.value.data)
            ) as result:
                await self.write_json(result.exchange)

    async def download_team_list(self):
        page = None
        while True:
            async with self.client.get_team_list(page=page) as result:
                pass
            next = result.value.meta.pagination.next
            for team in result.value.data:
                async with self.client.get_team_public(team_id=team.id) as result:
                    await self.write_json(result.exchange)
                async with self.client.get_team_public_solves(
                    team_id=team.id
                ) as result:
                    await self.write_json(result.exchange)
                async with self.client.get_team_public_fails(team_id=team.id) as result:
                    await self.write_json(result.exchange)
                async with self.client.get_team_public_awards(
                    team_id=team.id
                ) as result:
                    await self.write_json(result.exchange)
            if next is None:
                break
            page = next

    async def download_team_private(self):
        async with self.client.get_team_private() as result:
            await self.write_json(result.exchange)
        async with self.client.get_team_private_solves() as result:
            await self.write_json(result.exchange)
        async with self.client.get_team_private_fails() as result:
            await self.write_json(result.exchange)
        async with self.client.get_team_private_awards() as result:
            await self.write_json(result.exchange)

    async def download_user_list(self):
        page = None
        while True:
            async with self.client.get_user_list(page=page) as result:
                pass
            next = result.value.meta.pagination.next
            for user in result.value.data:
                async with self.client.get_user_public(user_id=user.id) as result:
                    await self.write_json(result.exchange)
            if next is None:
                break
            page = next

    async def download_user_private(self):
        async with self.client.get_user_private() as result:
            print(result.value)
            await self.write_json(result.exchange)

    async def download_challenge_file(self, url: str):
        params = ctfd_dl.challenges.challenge_file_url_to_params(url)
        async with self.client.get_files(
            path=params["path"], token=params["token"]
        ) as result:
            await self.write_file(
                result.exchange,
                urllib.parse.urlparse(result.exchange.request.url).path.split("/"),
            )

    async def write_json(self, exchange: ctfd_dl.http.exchanges.Exchange):
        await self.write_file(exchange, json_path(exchange.request.url))

    async def write_file(
        self, exchange: ctfd_dl.http.exchanges.Exchange, path: Iterable[str]
    ):
        destination = self.directory.joinpath(*path)
        if not destination.is_relative_to(self.directory):
            raise ctfd_dl.exceptions.Error
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(await exchange.response.read())


def json_path(url: str):
    result = urllib.parse.urlparse(url)
    # yield from result.path.split("/")
    for part in result.path.split("/"):
        yield part
    yield "index.json"
