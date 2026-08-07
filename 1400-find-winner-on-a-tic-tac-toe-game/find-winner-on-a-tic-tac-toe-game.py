class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""] * 3 for _ in range(3)]

        def check(player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True

            if all(board[i][i] == player for i in range(3)):
                return True

            if all(board[i][2 - i] == player for i in range(3)):
                return True

            return False

        for i, (r, c) in enumerate(moves):
            player = "X" if i % 2 == 0 else "O"
            board[r][c] = player

            if check(player):
                return "A" if player == "X" else "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"