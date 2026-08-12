class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []

        for i in range(len(mat)):
            soldiers = sum(mat[i])
            rows.append((soldiers, i))

        rows.sort()

        return [row[1] for row in rows[:k]]