class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        blocked = set()

        # Numbers that can never be good
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                blocked.add(fronts[i])

        answer = float('inf')

        # Find the smallest valid number
        for num in fronts:
            if num not in blocked:
                answer = min(answer, num)

        for num in backs:
            if num not in blocked:
                answer = min(answer, num)

        if answer == float('inf'):
            return 0

        return answer