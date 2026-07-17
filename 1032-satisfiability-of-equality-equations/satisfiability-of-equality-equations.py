class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        # Find the parent of a variable
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Join two sets
        def union(x, y):
            parent[find(x)] = find(y)

        # Initialize all variables
        for ch in "abcdefghijklmnopqrstuvwxyz":
            parent[ch] = ch

        # First process all "==" equations
        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])

        # Then check all "!=" equations
        for eq in equations:
            if eq[1] == "!":
                if find(eq[0]) == find(eq[3]):
                    return False

        return True