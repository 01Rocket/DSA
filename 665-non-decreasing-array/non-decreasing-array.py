class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changes = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                changes += 1

                if changes > 1:
                    return False

                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]

        return True