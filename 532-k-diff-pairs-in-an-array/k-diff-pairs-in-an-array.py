class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        count = Counter(nums)
        ans = 0

        if k == 0:
            for num in count:
                if count[num] > 1:
                    ans += 1
        else:
            for num in count:
                if num + k in count:
                    ans += 1

        return ans