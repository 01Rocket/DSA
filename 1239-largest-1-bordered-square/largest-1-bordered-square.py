class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = 1
                    down[i][j] = 1
                    if j + 1 < n:
                        right[i][j] += right[i][j + 1]
                    if i + 1 < m:
                        down[i][j] += down[i + 1][j]

        max_side = min(m, n)

        for size in range(max_side, 0, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if (right[i][j] >= size and
                        down[i][j] >= size and
                        right[i + size - 1][j] >= size and
                        down[i][j + size - 1] >= size):
                        return size * size

        return 0