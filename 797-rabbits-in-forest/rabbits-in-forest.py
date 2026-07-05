class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}

        for ans in answers:
            count[ans] = count.get(ans, 0) + 1

        total = 0

        for ans, freq in count.items():
            group = ans + 1
            groups_needed = (freq + group - 1) // group
            total += groups_needed * group

        return total