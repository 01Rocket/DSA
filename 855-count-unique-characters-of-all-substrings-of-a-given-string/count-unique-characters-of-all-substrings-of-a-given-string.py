class Solution:
    def uniqueLetterString(self, s: str) -> int:
        last = [-1] * 26
        prev = [-1] * 26
        ans = 0

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            ans += (i - last[idx]) * (last[idx] - prev[idx])
            prev[idx] = last[idx]
            last[idx] = i

        n = len(s)

        for i in range(26):
            ans += (n - last[i]) * (last[i] - prev[i])

        return ans