class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        if all(count.get(ch, 0) == target for ch in "QWER"):
            return 0

        ans = n
        left = 0

        for right in range(n):
            count[s[right]] -= 1

            while left <= right and all(count.get(ch, 0) <= target for ch in "QWER"):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1

        return ans