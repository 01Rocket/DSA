class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])

        row = [0] * m
        col = [0] * n

        # Count 1s in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        ans = 0

        # Find special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ans += 1

        return ans