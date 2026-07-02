class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    remaining = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            remaining.append(nums[k])

                    a = nums[i]
                    b = nums[j]

                    for value in [a + b, a - b, a * b]:
                        if solve(remaining + [value]):
                            return True

                    if abs(b) > 1e-6:
                        if solve(remaining + [a / b]):
                            return True

            return False

        return solve([float(x) for x in cards])