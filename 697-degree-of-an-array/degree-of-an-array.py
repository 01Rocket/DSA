class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            num = nums[i]

            if num not in first:
                first[num] = i

            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        answer = len(nums)

        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                answer = min(answer, length)

        return answer