class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k