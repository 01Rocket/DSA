class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)

        for row in matrix:
            if row[0] == 0:
                pattern = tuple(row)
            else:
                pattern = tuple(1 - x for x in row)

            count[pattern] += 1

        return max(count.values())