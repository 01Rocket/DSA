class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            steps = 0

            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1

                steps += 1

            return steps

        numbers = list(range(lo, hi + 1))

        numbers.sort(key=lambda x: (power(x), x))

        return numbers[k - 1]