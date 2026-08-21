class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            divisor_count = 0
            divisor_sum = 0

            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    divisor_count += 1
                    divisor_sum += i

                    # If i and num // i are different, count both
                    if i != num // i:
                        divisor_count += 1
                        divisor_sum += num // i

                    # No need to continue if there are already too many
                    if divisor_count > 4:
                        break

            if divisor_count == 4:
                total += divisor_sum

        return total