class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [""] * n

        order = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        for i, (index, _) in enumerate(order):
            if i == 0:
                ans[index] = "Gold Medal"
            elif i == 1:
                ans[index] = "Silver Medal"
            elif i == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(i + 1)

        return ans