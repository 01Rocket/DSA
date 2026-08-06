class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        # Count how many times each row and column is incremented
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        odd_count = 0

        # Check the parity of each cell
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 == 1:
                    odd_count += 1

        return odd_count