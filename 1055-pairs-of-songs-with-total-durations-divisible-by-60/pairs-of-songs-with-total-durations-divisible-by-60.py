class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        pairs = 0

        for t in time:
            rem = t % 60

            if rem == 0:
                pairs += count[0]
            else:
                pairs += count[60 - rem]

            count[rem] += 1

        return pairs