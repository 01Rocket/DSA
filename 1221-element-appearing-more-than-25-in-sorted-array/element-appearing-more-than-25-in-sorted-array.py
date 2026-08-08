class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0

        while i < n:
            count = 1

            while i + count < n and arr[i] == arr[i + count]:
                count += 1

            if count * 4 > n:
                return arr[i]

            i += count