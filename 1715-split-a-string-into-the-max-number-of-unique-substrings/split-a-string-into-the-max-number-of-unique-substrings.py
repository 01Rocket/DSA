class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def dfs(start):
            if start == len(s):
                return 0

            ans = 0

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]

                if sub not in seen:
                    seen.add(sub)
                    ans = max(ans, 1 + dfs(end))
                    seen.remove(sub)

            return ans

        return dfs(0)