class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        # Change negative numbers to positive
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # Find the smallest element
        smallest = min(nums)

        # If k is odd, flip the smallest element
        if k % 2 == 1:
            return sum(nums) - 2 * smallest

        return sum(nums)