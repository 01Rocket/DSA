class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}

        for i in range(len(digits)):
            last[digits[i]] = i

        for i in range(len(digits)):
            for d in range(9, int(digits[i]), -1):
                if str(d) in last and last[str(d)] > i:
                    j = last[str(d)]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num