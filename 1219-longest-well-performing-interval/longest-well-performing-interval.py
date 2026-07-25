class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = 0
        first = {}
        longest = 0

        for i in range(len(hours)):
            if hours[i] > 8:
                prefix += 1
            else:
                prefix -= 1

            if prefix > 0:
                longest = i + 1
            else:
                if prefix not in first:
                    first[prefix] = i

                if (prefix - 1) in first:
                    longest = max(longest, i - first[prefix - 1])

        return longest