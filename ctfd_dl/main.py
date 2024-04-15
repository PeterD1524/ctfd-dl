import argparse
import asyncio
import getpass
import pathlib

import ctfd_dl.core
import ctfd_dl.exceptions


async def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output-directory", type=pathlib.Path, required=True)
    args = parser.parse_args()
    base_url = args.base_url
    if not isinstance(base_url, str):
        raise ctfd_dl.exceptions.Error
    output_directory = args.output_directory
    if not isinstance(output_directory, pathlib.Path):
        raise ctfd_dl.exceptions.Error
    async with ctfd_dl.core.client(base_url=base_url) as client:
        await client.login(
            name=getpass.getpass("name: "), password=getpass.getpass("password: ")
        )
        downloader = ctfd_dl.core.Downloader(client=client, directory=output_directory)
        await downloader.download()


if __name__ == "__main__":
    asyncio.run(main())
