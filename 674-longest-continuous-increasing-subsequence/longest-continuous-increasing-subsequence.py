class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                current = 1

            if current > longest:
                longest = current

        return longest