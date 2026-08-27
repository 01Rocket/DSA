class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]

        # Generate Fibonacci numbers up to k
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        count = 0

        # Start from the largest Fibonacci number
        for num in reversed(fib):
            if num <= k:
                k -= num
                count += 1

            if k == 0:
                break

        return count