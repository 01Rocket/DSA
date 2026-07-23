class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb

        for i in range(len(s1)):
            union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        ans = []

        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            ans.append(chr(root + ord('a')))

        return "".join(ans)