class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # Arrange the stones in increasing order
        stones = sorted([a, b, c])
        x, y, z = stones

        left_gap = y - x
        right_gap = z - y

        # Minimum moves
        if left_gap == 1 and right_gap == 1:
            min_moves = 0
        elif left_gap <= 2 or right_gap <= 2:
            min_moves = 1
        else:
            min_moves = 2

        # Maximum moves
        max_moves = (left_gap - 1) + (right_gap - 1)

        return [min_moves, max_moves]