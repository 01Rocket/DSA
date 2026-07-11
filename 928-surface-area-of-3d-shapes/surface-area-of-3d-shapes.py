class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                height = grid[i][j]

                if height > 0:
                    # Top and bottom faces
                    area += 2

                    # Four side faces
                    area += height * 4

                    # Remove shared sides with neighbors
                    if i > 0:
                        area -= 2 * min(height, grid[i - 1][j])

                    if j > 0:
                        area -= 2 * min(height, grid[i][j - 1])

        return area