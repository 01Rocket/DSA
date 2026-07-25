class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []

        # Add elements in the order of arr2
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        # Add remaining elements in sorted order
        for num in sorted(count):
            result.extend([num] * count[num])

        return result