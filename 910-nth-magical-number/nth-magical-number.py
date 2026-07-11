class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        lcm = (a * b) // gcd(a, b)

        left = min(a, b)
        right = n * min(a, b)

        while left < right:
            mid = (left + right) // 2

            count = mid // a + mid // b - mid // lcm

            if count < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD