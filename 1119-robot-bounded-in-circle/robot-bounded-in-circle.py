class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0

        # North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        for move in instructions:
            if move == "G":
                dx, dy = directions[direction]
                x += dx
                y += dy
            elif move == "L":
                direction = (direction - 1) % 4
            else:  # "R"
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0