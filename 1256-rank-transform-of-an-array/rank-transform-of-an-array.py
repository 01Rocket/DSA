class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))

        rank = {}
        for i, value in enumerate(sorted_arr):
            rank[value] = i + 1

        return [rank[value] for value in arr]