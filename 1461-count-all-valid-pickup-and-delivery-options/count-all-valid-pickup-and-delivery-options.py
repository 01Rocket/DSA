class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        answer = 1

        for i in range(1, n + 1):
            answer = answer * i * (2 * i - 1) % MOD

        return answer