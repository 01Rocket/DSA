class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        ones = s.count('1')
        n = len(s)

        if ones % 3 != 0:
            return 0

        if ones == 0:
            return ((n - 1) * (n - 2) // 2) % MOD

        k = ones // 3
        count1 = count2 = 0
        seen = 0

        for ch in s:
            if ch == '1':
                seen += 1

            if seen == k:
                count1 += 1
            elif seen == 2 * k:
                count2 += 1

        return (count1 * count2) % MOD