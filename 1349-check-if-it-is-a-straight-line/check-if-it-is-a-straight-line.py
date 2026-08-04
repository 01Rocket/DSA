class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        dx = x2 - x1
        dy = y2 - y1

        for x, y in coordinates[2:]:
            if (x - x1) * dy != (y - y1) * dx:
                return False

        return True