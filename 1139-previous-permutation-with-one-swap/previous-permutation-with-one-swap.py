class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        # Find the first position from the right where arr[i] > arr[i + 1]
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                index = -1

                # Find the largest element smaller than arr[i]
                for j in range(i + 1, n):
                    if arr[j] < arr[i]:
                        if index == -1 or arr[j] >= arr[index]:
                            index = j

                # Avoid swapping with duplicate values
                while index > i + 1 and arr[index] == arr[index - 1]:
                    index -= 1

                arr[i], arr[index] = arr[index], arr[i]
                break

        return arr