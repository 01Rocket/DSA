class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the rook's position
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    row, col = i, j
                    break

        count = 0

        # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            r = row + dr
            c = col + dc

            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == "B":
                    break
                if board[r][c] == "p":
                    count += 1
                    break

                r += dr
                c += dc

        return count