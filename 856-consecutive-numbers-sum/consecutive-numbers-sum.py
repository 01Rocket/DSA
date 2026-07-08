class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        length = 1

        while length * (length - 1) // 2 < n:
            remaining = n - (length * (length - 1) // 2)

            if remaining % length == 0:
                count += 1

            length += 1

        return count