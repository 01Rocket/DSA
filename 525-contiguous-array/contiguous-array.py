class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}
        count = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in first_index:
                ans = max(ans, i - first_index[count])
            else:
                first_index[count] = i

        return ans