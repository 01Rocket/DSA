class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count = 0
        last_valid = -1
        last_invalid = -1

        for i in range(len(nums)):
            if left <= nums[i] <= right:
                last_valid = i

            if nums[i] > right:
                last_invalid = i

            count += max(0, last_valid - last_invalid)

        return count