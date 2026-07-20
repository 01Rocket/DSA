class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = []

        # Store all cell coordinates
        for i in range(rows):
            for j in range(cols):
                cells.append([i, j])

        # Sort based on Manhattan distance
        cells.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))

        return cells