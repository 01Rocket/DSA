class Solution:
    def minOperations(self, nums: list[int]) -> int:
        increments = 0
        max_bits = 0

        for num in nums:
            increments += num.bit_count()
            max_bits = max(max_bits, num.bit_length())

        if max_bits == 0:
            return 0

        return increments + max_bits - 1