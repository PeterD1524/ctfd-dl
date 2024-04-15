import dataclasses


@dataclasses.dataclass
class Aspects:
    create: str
    update: str
    view: str


@dataclasses.dataclass
class TypeData:
    id: str
    name: str
    templates: Aspects
    scripts: Aspects


@dataclasses.dataclass
class BaseChallengeRead:
    id: int
    name: str
    value: str
    description: str
    connection_info: str
    next_id: int
    category: str
    state: str
    max_attempts: int
    type: str
    type_data: TypeData
