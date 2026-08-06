class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        current_gcd = nums[0]

        for num in nums[1:]:
            current_gcd = gcd(current_gcd, num)

        return current_gcd == 1