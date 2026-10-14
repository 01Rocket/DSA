class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        prev = '0'

        for bit in target:
            if bit != prev:
                flips += 1
                prev = bit

        return flips