class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            count = 0

            for j in range(m * k):
                if arr[i + j] != arr[i + j % m]:
                    break
                count += 1

            if count == m * k:
                return True

        return False