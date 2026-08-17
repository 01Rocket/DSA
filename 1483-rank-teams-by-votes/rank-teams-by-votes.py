class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = votes[0]
        n = len(teams)

        count = {team: [0] * n for team in teams}

        # Count how many times each team gets each position
        for vote in votes:
            for i in range(n):
                count[vote[i]][i] += 1

        teams = sorted(
            teams,
            key=lambda team: tuple(-x for x in count[team]) + (team,)
        )

        return "".join(teams)