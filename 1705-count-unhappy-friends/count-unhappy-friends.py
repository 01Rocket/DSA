class Solution:
    def unhappyFriends(self, n: int, preferences: list[list[int]], pairs: list[list[int]]) -> int:
        partner = [0] * n

        # Store current partners
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        ans = 0

        for x in range(n):
            y = partner[x]

            # Check friends preferred over current partner
            for u in preferences[x]:
                if u == y:
                    break

                v = partner[u]

                # Check if u prefers x over their partner
                if preferences[u].index(x) < preferences[u].index(v):
                    ans += 1
                    break

        return ans 