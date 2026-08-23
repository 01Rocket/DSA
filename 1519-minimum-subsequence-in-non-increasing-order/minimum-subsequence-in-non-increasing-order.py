class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        total = sum(nums)
        selected_sum = 0
        answer = []

        for num in nums:
            selected_sum += num
            answer.append(num)

            if selected_sum > total - selected_sum:
                break

        return answer