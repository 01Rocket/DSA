class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        has_incoming = [False] * n

        for u, v in edges:
            has_incoming[v] = True

        return [i for i in range(n) if not has_incoming[i]]