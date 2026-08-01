class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px

        # Connect all indices
        for x, y in pairs:
            union(x, y)

        # Group indices by their parent
        groups = {}

        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        ans = list(s)

        # Sort characters inside each group
        for indices in groups.values():
            chars = []

            for i in indices:
                chars.append(s[i])

            indices.sort()
            chars.sort()

            for i in range(len(indices)):
                ans[indices[i]] = chars[i]

        return "".join(ans)