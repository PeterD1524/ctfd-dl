import dataclasses
from typing import Any, cast

import pydantic


@dataclasses.dataclass
class TypeAdapter:
    inner: dict[Any, pydantic.TypeAdapter[Any]]

    def get[T](self, type: type[T]):
        inner = self.inner
        try:
            adapter = inner[type]
        except KeyError:
            adapter = pydantic.TypeAdapter(type=type)
            self.inner[type] = adapter
        else:
            adapter = cast(pydantic.TypeAdapter[T], adapter)
        return adapter

    def validate_json[T](self, type: type[T], data: bytes):
        return self.get(type).validate_json(data, strict=True)


def type_adapter():
    return TypeAdapter({})
