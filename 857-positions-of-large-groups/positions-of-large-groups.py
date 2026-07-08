class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        n = len(s)
        start = 0

        while start < n:
            end = start

            while end < n and s[end] == s[start]:
                end += 1

            if end - start >= 3:
                result.append([start, end - 1])

            start = end

        return result