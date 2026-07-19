class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        current = 0

        for bit in nums:
            current = (current * 2 + bit) % 5
            answer.append(current == 0)

        return answer