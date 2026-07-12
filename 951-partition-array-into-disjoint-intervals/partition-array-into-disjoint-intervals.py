class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        max_so_far = nums[0]
        partition = 0

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far, nums[i])

            if nums[i] < left_max:
                left_max = max_so_far
                partition = i

        return partition + 1