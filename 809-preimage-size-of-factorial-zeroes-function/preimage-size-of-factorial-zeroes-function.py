class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_zeros(x):
            res = 0
            while x > 0:
                x //= 5
                res += x
            return res

        left, right = 0, 5 * (k + 1)

        while left <= right:
            mid = (left + right) // 2
            if count_zeros(mid) < k:
                left = mid + 1
            else:
                right = mid - 1

        # check if solution exists
        if count_zeros(left) == k:
            return 5
        return 0