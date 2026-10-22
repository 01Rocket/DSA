class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        ans = 0
        seen = {0: -1}

        for i, ch in enumerate(s):
            mask ^= 1 << int(ch)

            if mask in seen:
                ans = max(ans, i - seen[mask])

            for d in range(10):
                prev = mask ^ (1 << d)
                if prev in seen:
                    ans = max(ans, i - seen[prev])

            if mask not in seen:
                seen[mask] = i

        return ans