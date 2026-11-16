class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0
        ans = 0

        for _ in range(n):
            # Find the unvisited point with minimum distance
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            visited[u] = True
            ans += min_dist[u]

            # Update distances to other unvisited points
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + \
                           abs(points[u][1] - points[v][1])

                    min_dist[v] = min(min_dist[v], dist)

        return ans