class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def count_moves(start):
            moves = 0

            for i in range(start, len(nums), 2):
                left = nums[i - 1] if i > 0 else float("inf")
                right = nums[i + 1] if i < len(nums) - 1 else float("inf")

                limit = min(left, right) - 1

                if nums[i] > limit:
                    moves += nums[i] - limit

            return moves

        return min(count_moves(0), count_moves(1))