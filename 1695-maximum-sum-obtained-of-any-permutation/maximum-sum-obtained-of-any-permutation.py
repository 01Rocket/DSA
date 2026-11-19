class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)

        # Count frequency of each index
        for l, r in requests:
            diff[l] += 1
            diff[r + 1] -= 1

        # Calculate actual frequencies
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # Sort nums and frequencies
        nums.sort()
        freq = sorted(diff[:n])

        # Calculate maximum sum
        return sum(a * b for a, b in zip(nums, freq)) % (10**9 + 7)