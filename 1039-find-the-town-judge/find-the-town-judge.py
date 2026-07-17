class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        # Count incoming and outgoing trust
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        # Judge trusts nobody and is trusted by everyone else
        for person in range(1, n + 1):
            if indegree[person] == n - 1 and outdegree[person] == 0:
                return person

        return -1