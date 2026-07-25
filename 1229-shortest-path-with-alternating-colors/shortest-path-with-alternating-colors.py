class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for u, v in redEdges:
            red[u].append(v)

        for u, v in blueEdges:
            blue[u].append(v)

        ans = [-1] * n
        visited = set()

        q = deque()
        q.append((0, 0, -1))   # node, distance, last colour
        q.append((0, 0, 1))

        while q:
            node, dist, last = q.popleft()

            if (node, last) in visited:
                continue
            visited.add((node, last))

            if ans[node] == -1:
                ans[node] = dist

            if last != 0:
                for nxt in red[node]:
                    q.append((nxt, dist + 1, 0))

            if last != 1:
                for nxt in blue[node]:
                    q.append((nxt, dist + 1, 1))

        return ans