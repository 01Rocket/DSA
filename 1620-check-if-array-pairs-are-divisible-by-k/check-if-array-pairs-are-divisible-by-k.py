class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        rem = [0] * k

        for x in arr:
            rem[x % k] += 1

        if rem[0] % 2:
            return False

        for i in range(1, k):
            if rem[i] != rem[k - i]:
                return False

        return True