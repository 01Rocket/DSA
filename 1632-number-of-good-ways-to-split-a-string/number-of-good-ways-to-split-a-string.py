class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right = set(s)
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        count = 0

        for i in range(len(s) - 1):
            ch = s[i]
            left.add(ch)
            freq[ch] -= 1

            if freq[ch] == 0:
                right.remove(ch)

            if len(left) == len(right):
                count += 1

        return count