class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_closest(n):
            i = int(n ** 0.5)

            while n % i != 0:
                i -= 1

            return [i, n // i]

        a = find_closest(num + 1)
        b = find_closest(num + 2)

        if abs(a[0] - a[1]) <= abs(b[0] - b[1]):
            return a

        return b