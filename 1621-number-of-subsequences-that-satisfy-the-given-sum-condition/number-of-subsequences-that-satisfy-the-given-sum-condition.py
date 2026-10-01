class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()

        n = len(nums)
        power = [1] * n

        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        left, right = 0, n - 1
        ans = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                # nums[left] is the minimum.
                # Every element between left and right can be chosen or skipped.
                ans = (ans + power[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return ans