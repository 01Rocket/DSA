class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        longest = 0

        for i in range(len(nums)):
            if not visited[i]:
                length = 0
                current = i

                while not visited[current]:
                    visited[current] = True
                    current = nums[current]
                    length += 1

                longest = max(longest, length)

        return longest