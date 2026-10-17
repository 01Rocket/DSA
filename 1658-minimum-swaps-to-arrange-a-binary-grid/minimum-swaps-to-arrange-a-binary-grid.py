class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        zeros = []

        # Count trailing zeros in each row
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        swaps = 0

        # Place a suitable row at each position
        for i in range(n):
            needed = n - i - 1
            j = i

            while j < n and zeros[j] < needed:
                j += 1

            if j == n:
                return -1

            swaps += j - i

            # Move the selected row to position i
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                j -= 1

        return swaps