class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0

        for i in range(n):
            count = (i + 1) * (n - i)
            odd_count = (count + 1) // 2
            total += arr[i] * odd_count

        return total