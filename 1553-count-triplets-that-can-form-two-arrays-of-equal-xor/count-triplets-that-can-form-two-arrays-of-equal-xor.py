class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0

        for i in range(n):
            xor_value = 0

            for k in range(i, n):
                xor_value ^= arr[k]

                if xor_value == 0:
                    count += k - i

        return count