class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        removed = 0

        for count in sorted(freq.values()):
            if k >= count:
                k -= count
                removed += 1
            else:
                break

        return len(freq) - removed