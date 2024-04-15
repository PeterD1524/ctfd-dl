import dataclasses

import ctfd_dl.api.v1.challenges
import ctfd_dl.api.v1.hints
import ctfd_dl.api.v1.scoreboard
import ctfd_dl.api.v1.teams
import ctfd_dl.api.v1.users
import ctfd_dl.app
import ctfd_dl.http.requests


def api_request(app: ctfd_dl.app.App, request: ctfd_dl.http.requests.Request):
    return app.base_url.request(app.api.request(request))


@dataclasses.dataclass
class Requests:
    app: ctfd_dl.app.App

    def get_challenge_list(
        self, params: ctfd_dl.api.v1.challenges.GetChallengeListParams
    ):
        return api_request(
            self.app,
            self.app.api.challenges.request(
                self.app.api.challenges.get_challenge_list.request(params)
            ),
        )

    def get_challenge(self, params: ctfd_dl.api.v1.challenges.GetChallengeParams):
        return api_request(
            self.app,
            self.app.api.challenges.request(
                self.app.api.challenges.get_challenge.request(params)
            ),
        )

    def get_challenge_solves(
        self, params: ctfd_dl.api.v1.challenges.GetChallengeSolvesParams
    ):
        return api_request(
            self.app,
            self.app.api.challenges.request(
                self.app.api.challenges.get_challenge_solves.request(params)
            ),
        )

    def get_hint(self, params: ctfd_dl.api.v1.hints.GetHintParams):
        return api_request(
            self.app,
            self.app.api.hints.request(self.app.api.hints.get_hint.request(params)),
        )

    def get_scoreboard_list(
        self, params: ctfd_dl.api.v1.scoreboard.GetScoreboardListParams
    ):
        return api_request(
            self.app,
            self.app.api.scoreboard.request(
                self.app.api.scoreboard.get_scoreboard_list.request(params)
            ),
        )

    def get_scoreboard_detail(
        self, params: ctfd_dl.api.v1.scoreboard.GetScoreboardDetailParams
    ):
        return api_request(
            self.app,
            self.app.api.scoreboard.request(
                self.app.api.scoreboard.get_scoreboard_detail.request(params)
            ),
        )

    def get_team_list(self, params: ctfd_dl.api.v1.teams.GetTeamListParams):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_list.request(params)
            ),
        )

    def get_team_public(self, params: ctfd_dl.api.v1.teams.GetTeamPublicParams):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_public.request(params)
            ),
        )

    def get_team_private(self, params: ctfd_dl.api.v1.teams.GetTeamPrivateParams):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_private.request(params)
            ),
        )

    def get_team_private_solves(
        self, params: ctfd_dl.api.v1.teams.GetTeamPrivateSolvesParams
    ):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_private_solves.request(params)
            ),
        )

    def get_team_private_fails(
        self, params: ctfd_dl.api.v1.teams.GetTeamPrivateFailsParams
    ):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_private_fails.request(params)
            ),
        )

    def get_team_private_fails_awards(
        self, params: ctfd_dl.api.v1.teams.GetTeamPrivateAwardsParams
    ):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_private_awards.request(params)
            ),
        )

    def get_team_public_solves(
        self, params: ctfd_dl.api.v1.teams.GetTeamPublicSolvesParams
    ):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_public_solves.request(params)
            ),
        )

    def get_team_public_fails(
        self, params: ctfd_dl.api.v1.teams.GetTeamPublicFailsParams
    ):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_public_fails.request(params)
            ),
        )

    def get_team_public_awards(
        self, params: ctfd_dl.api.v1.teams.GetTeamPublicAwardsParams
    ):
        return api_request(
            self.app,
            self.app.api.teams.request(
                self.app.api.teams.get_team_public_awards.request(params)
            ),
        )

    def get_user_list(self, params: ctfd_dl.api.v1.users.GetUserListParams):
        return api_request(
            self.app,
            self.app.api.users.request(
                self.app.api.users.get_user_list.request(params)
            ),
        )

    def get_user_public(self, params: ctfd_dl.api.v1.users.GetUserPublicParams):
        return api_request(
            self.app,
            self.app.api.users.request(
                self.app.api.users.get_user_public.request(params)
            ),
        )

    def get_user_private(self, params: ctfd_dl.api.v1.users.GetUserPrivateParams):
        return api_request(
            self.app,
            self.app.api.users.request(
                self.app.api.users.get_user_private.request(params)
            ),
        )
