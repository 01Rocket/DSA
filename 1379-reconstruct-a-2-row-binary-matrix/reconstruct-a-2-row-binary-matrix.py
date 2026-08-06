class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        top = [0] * n
        bottom = [0] * n

        # Fill columns where both rows must have 1
        for i in range(n):
            if colsum[i] == 2:
                top[i] = 1
                bottom[i] = 1
                upper -= 1
                lower -= 1

        # If impossible, return empty list
        if upper < 0 or lower < 0:
            return []

        # Fill columns where only one row has 1
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    top[i] = 1
                    upper -= 1
                else:
                    bottom[i] = 1
                    lower -= 1

        # Check if all required 1's are used
        if upper == 0 and lower == 0:
            return [top, bottom]

        return []