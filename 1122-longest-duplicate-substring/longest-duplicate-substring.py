class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(ch) - ord('a') for ch in s]

        base = 26
        mod = (1 << 63) - 1

        def check(length):
            if length == 0:
                return -1

            h = 0
            power = 1

            for i in range(length):
                h = (h * base + nums[i]) % mod
                power = (power * base) % mod

            seen = {h}

            for i in range(length, n):
                h = (h * base - nums[i - length] * power + nums[i]) % mod

                if h in seen:
                    return i - length + 1

                seen.add(h)

            return -1

        left, right = 1, n - 1
        start = -1
        max_len = 0

        while left <= right:
            mid = (left + right) // 2
            pos = check(mid)

            if pos != -1:
                start = pos
                max_len = mid
                left = mid + 1
            else:
                right = mid - 1

        if start == -1:
            return ""

        return s[start:start + max_len]