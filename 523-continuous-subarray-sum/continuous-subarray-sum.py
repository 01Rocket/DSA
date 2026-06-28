class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            rem = prefix_sum % k

            if rem in remainder_index:
                if i - remainder_index[rem] > 1:
                    return True
            else:
                remainder_index[rem] = i

        return False