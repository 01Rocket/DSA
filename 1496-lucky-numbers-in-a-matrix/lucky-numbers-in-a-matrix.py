class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]

        col_max = []
        for j in range(len(matrix[0])):
            maximum = matrix[0][j]

            for i in range(len(matrix)):
                maximum = max(maximum, matrix[i][j])

            col_max.append(maximum)

        return [num for num in row_min if num in col_max]