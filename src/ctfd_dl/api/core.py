import dataclasses

import ctfd_dl.api.v1.challenges
import ctfd_dl.api.v1.hints
import ctfd_dl.api.v1.scoreboard
import ctfd_dl.api.v1.teams
import ctfd_dl.api.v1.users
import ctfd_dl.namespaces
import ctfd_dl.type_adapters


@dataclasses.dataclass
class ApiV1(ctfd_dl.namespaces.Namespace):
    challenges: ctfd_dl.api.v1.challenges.Challenges
    hints: ctfd_dl.api.v1.hints.Hints
    scoreboard: ctfd_dl.api.v1.scoreboard.Scoreboard
    teams: ctfd_dl.api.v1.teams.Teams
    users: ctfd_dl.api.v1.users.Users


def api_v1(type_adapter: ctfd_dl.type_adapters.TypeAdapter):
    return ApiV1(
        path="/api/v1",
        challenges=ctfd_dl.api.v1.challenges.Challenges(
            path="/challenges",
            get_challenge_list=ctfd_dl.api.v1.challenges.GetChallengeList(type_adapter),
            get_challenge=ctfd_dl.api.v1.challenges.GetChallenge(type_adapter),
            get_challenge_solves=ctfd_dl.api.v1.challenges.GetChallengeSolves(
                type_adapter
            ),
        ),
        hints=ctfd_dl.api.v1.hints.Hints(
            path="/hints", get_hint=ctfd_dl.api.v1.hints.GetHint(type_adapter)
        ),
        scoreboard=ctfd_dl.api.v1.scoreboard.Scoreboard(
            path="/scoreboard",
            get_scoreboard_list=ctfd_dl.api.v1.scoreboard.GetScoreboardList(
                type_adapter
            ),
            get_scoreboard_detail=ctfd_dl.api.v1.scoreboard.GetScoreboardDetail(
                type_adapter
            ),
        ),
        teams=ctfd_dl.api.v1.teams.Teams(
            path="/teams",
            get_team_list=ctfd_dl.api.v1.teams.GetTeamList(type_adapter),
            get_team_public=ctfd_dl.api.v1.teams.GetTeamPublic(type_adapter),
            get_team_private=ctfd_dl.api.v1.teams.GetTeamPrivate(type_adapter),
            get_team_private_solves=ctfd_dl.api.v1.teams.GetTeamPrivateSolves(
                type_adapter
            ),
            get_team_private_fails=ctfd_dl.api.v1.teams.GetTeamPrivateFails(
                type_adapter
            ),
            get_team_private_awards=ctfd_dl.api.v1.teams.GetTeamPrivateAwards(
                type_adapter
            ),
            get_team_public_solves=ctfd_dl.api.v1.teams.GetTeamPublicSolves(
                type_adapter
            ),
            get_team_public_fails=ctfd_dl.api.v1.teams.GetTeamPublicFails(type_adapter),
            get_team_public_awards=ctfd_dl.api.v1.teams.GetTeamPublicAwards(
                type_adapter
            ),
        ),
        users=ctfd_dl.api.v1.users.Users(
            path="/users",
            get_user_list=ctfd_dl.api.v1.users.GetUserList(type_adapter),
            get_user_public=ctfd_dl.api.v1.users.GetUserPublic(type_adapter),
            get_user_private=ctfd_dl.api.v1.users.GetUserPrivate(type_adapter),
        ),
    )
