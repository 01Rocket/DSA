class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        while s != "1":
            if s[-1] == "0":
                # Even number: divide by 2
                s = s[:-1]
            else:
                # Odd number: add 1
                s = bin(int(s, 2) + 1)[2:]

            steps += 1

        return steps