class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        odd = 0

        for freq in count:
            if freq % 2 == 1:
                odd += 1

        return odd <= k