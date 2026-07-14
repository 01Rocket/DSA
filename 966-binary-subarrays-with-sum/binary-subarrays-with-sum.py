class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        current_sum = 0
        answer = 0

        for num in nums:
            current_sum += num

            if current_sum - goal in count:
                answer += count[current_sum - goal]

            if current_sum in count:
                count[current_sum] += 1
            else:
                count[current_sum] = 1

        return answer