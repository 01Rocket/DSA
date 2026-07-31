class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums):
            current = 0
            best = 0

            for num in nums:
                current = max(0, current + num)
                best = max(best, current)

            return best

        total_sum = sum(arr)

        # Maximum subarray for one copy
        one = kadane(arr)

        if k == 1:
            return one % MOD

        # Maximum subarray for two copies
        two = kadane(arr + arr)

        if total_sum > 0:
            answer = two + (k - 2) * total_sum
        else:
            answer = two

        return answer % MOD