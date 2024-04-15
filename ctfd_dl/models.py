import dataclasses
from typing import Any


@dataclasses.dataclass
class Notifications:
    id: int
    title: str | None
    content: str | None
    date: str | None
    user_id: int | None
    team_id: int | None


@dataclasses.dataclass
class Pages:
    id: int
    title: str | None
    route: str | None
    content: str | None
    draft: bool | None
    hidden: bool | None
    auth_required: bool | None
    format: str | None
    link_target: str | None


@dataclasses.dataclass
class Challenges:
    id: int
    name: str | None
    description: str | None
    connection_info: str | None
    next_id: int | None
    max_attempts: int | None
    value: int | None
    category: str | None
    type: str | None
    state: str
    requirements: Any | None


@dataclasses.dataclass
class Hints:
    id: int
    type: str | None
    challenge_id: int | None
    content: str | None
    cost: int | None
    requirements: Any | None


@dataclasses.dataclass
class Awards:
    id: int
    user_id: int | None
    team_id: int | None
    type: str | None
    name: str | None
    description: str | None
    date: str | None
    value: int | None
    category: str | None
    icon: str | None
    requirements: Any | None


@dataclasses.dataclass
class Tags:
    id: int
    challenge_id: int | None
    value: str | None


@dataclasses.dataclass
class Topics:
    id: int
    value: str | None


@dataclasses.dataclass
class ChallengeTopics:
    id: int
    challenge_id: int | None
    topic_id: int | None


@dataclasses.dataclass
class Files:
    id: int
    type: str | None
    location: str | None
    sha1sum: str | None


@dataclasses.dataclass
class Flags:
    id: int
    challenge_id: int | None
    type: str | None
    content: str | None
    data: str | None


@dataclasses.dataclass
class Users:
    id: int
    oauth_id: int | None
    name: str | None
    password: str | None
    email: str | None
    type: str | None
    secret: str | None
    website: str | None
    affiliation: str | None
    country: str | None
    bracket_id: int | None
    hidden: bool | None
    banned: bool | None
    verified: bool | None
    language: str | None
    team_id: int | None
    created: str | None


@dataclasses.dataclass
class Teams:
    id: int
    oauth_id: int | None
    name: str | None
    email: str | None
    password: str | None
    secret: str | None
    website: str | None
    affiliation: str | None
    country: str | None
    bracket_id: int | None
    hidden: bool | None
    banned: bool | None
    captain_id: int | None
    created: str | None


@dataclasses.dataclass
class Submissions:
    id: int
    challenge_id: int | None
    user_id: int | None
    team_id: int | None
    ip: str | None
    provided: str | None
    type: str | None
    date: str | None


@dataclasses.dataclass
class Unlocks:
    id: int
    user_id: int | None
    team_id: int | None
    target: int | None
    date: str | None
    type: str | None


@dataclasses.dataclass
class Tracking:
    id: int
    type: str | None
    ip: str | None
    user_id: int | None
    date: str | None


@dataclasses.dataclass
class Configs:
    id: int
    key: str | None
    value: str | None


@dataclasses.dataclass
class Tokens:
    id: int
    type: str | None
    user_id: int | None
    created: str | None
    expiration: str | None
    description: str | None
    value: str | None


@dataclasses.dataclass
class Comments:
    id: int
    type: str | None
    content: str | None
    date: str | None
    author_id: int | None


@dataclasses.dataclass
class Fields:
    id: int
    name: str | None
    type: str | None
    field_type: str | None
    description: str | None
    required: bool | None
    public: bool | None
    editable: bool | None


@dataclasses.dataclass
class FieldEntries:
    id: int
    type: str | None
    value: Any | None
    field_id: int | None


@dataclasses.dataclass
class Brackets:
    id: int
    name: str | None
    description: str | None
    type: str | None
