class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def findMax(L, M):
            maxL = prefix[L] - prefix[0]
            answer = 0

            for i in range(L + M, n + 1):
                maxL = max(maxL, prefix[i - M] - prefix[i - M - L])
                currentM = prefix[i] - prefix[i - M]
                answer = max(answer, maxL + currentM)

            return answer

        return max(findMax(firstLen, secondLen),
                   findMax(secondLen, firstLen))