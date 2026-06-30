class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # Product of the three largest numbers
        product1 = nums[-1] * nums[-2] * nums[-3]

        # Product of two smallest numbers and the largest number
        product2 = nums[0] * nums[1] * nums[-1]

        # Return the larger product
        return max(product1, product2)