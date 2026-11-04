class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        n = len(arr)
        length = [0] * (n + 2)
        count = 0
        ans = -1

        for step, pos in enumerate(arr, 1):
            left = length[pos - 1]
            right = length[pos + 1]

            if left == m:
                count -= 1

            if right == m:
                count -= 1

            new_length = left + right + 1

            length[pos - left] = new_length
            length[pos + right] = new_length

            if new_length == m:
                count += 1

            if count > 0:
                ans = step

        return ans