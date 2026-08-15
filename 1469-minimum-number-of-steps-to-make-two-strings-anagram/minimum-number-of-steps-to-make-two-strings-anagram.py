class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        return sum(x for x in count if x > 0)