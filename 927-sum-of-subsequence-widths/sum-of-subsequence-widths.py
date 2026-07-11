class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        nums.sort()
        n = len(nums)

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        ans = 0

        for i in range(n):
            ans += nums[i] * (power[i] - power[n - i - 1])
            ans %= MOD

        return ans