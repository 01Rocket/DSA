class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x * y // gcd(x, y)

        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)

        def count(num):
            return (num // a +
                    num // b +
                    num // c -
                    num // ab -
                    num // ac -
                    num // bc +
                    num // abc)

        left, right = 1, 2 * 10**9

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1

        return left