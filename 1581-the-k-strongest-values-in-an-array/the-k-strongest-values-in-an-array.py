class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        n = len(arr)
        centre = arr[(n - 1) // 2]

        # Sort by:  Distance from centre & Value itself
        arr.sort(key=lambda x: (abs(x - centre), x), reverse=True)

        return arr[:k]