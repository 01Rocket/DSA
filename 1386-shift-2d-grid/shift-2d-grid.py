class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        # Convert grid to a single list
        nums = []
        for row in grid:
            nums.extend(row)

        # Shift the list
        total = m * n
        k = k % total
        nums = nums[-k:] + nums[:-k]

        # Convert back to 2D grid
        result = []
        index = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(nums[index])
                index += 1
            result.append(row)

        return result