class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        pos = 0
        neg = 0
        ans = 0

        for num in nums:
            if num == 0:
                pos = 0
                neg = 0

            elif num > 0:
                pos += 1
                if neg > 0:
                    neg += 1

            else:
                pos, neg = (
                    neg + 1 if neg > 0 else 0,
                    pos + 1
                )

            ans = max(ans, pos)

        return ans