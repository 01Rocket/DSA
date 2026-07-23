class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = []

        for num in arr:
            temp.append(num)
            if num == 0:
                temp.append(0)

        for i in range(len(arr)):
            arr[i] = temp[i]