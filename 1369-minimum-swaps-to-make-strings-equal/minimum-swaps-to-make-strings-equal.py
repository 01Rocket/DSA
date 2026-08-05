class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1

        # If total mismatches are odd, it's impossible
        if (xy + yx) % 2 != 0:
            return -1

        # Pairs of same type need one swap each
        swaps = (xy // 2) + (yx // 2)

        # One leftover xy and one leftover yx need two swaps
        if xy % 2 == 1:
            swaps += 2

        return swaps