class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        max_len = num.bit_length()

        for m in range(max_len, 1, -1):
            left, right = 2, int(num ** (1 / (m - 1))) + 1

            while left <= right:
                mid = (left + right) // 2

                total = 1
                curr = 1

                for _ in range(m - 1):
                    curr *= mid
                    total += curr
                    if total > num:
                        break

                if total == num:
                    return str(mid)
                elif total < num:
                    left = mid + 1
                else:
                    right = mid - 1

        return str(num - 1)