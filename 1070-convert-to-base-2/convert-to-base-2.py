class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        result = ""

        while n != 0:
            remainder = n % 2
            result = str(remainder) + result
            n = (n - remainder) // -2

        return result