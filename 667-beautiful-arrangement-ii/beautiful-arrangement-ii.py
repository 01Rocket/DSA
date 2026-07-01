class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = []

        for i in range(1, n - k):
            result.append(i)

        left = n - k
        right = n

        while left <= right:
            result.append(left)
            left += 1

            if left <= right:
                result.append(right)
                right -= 1

        return result