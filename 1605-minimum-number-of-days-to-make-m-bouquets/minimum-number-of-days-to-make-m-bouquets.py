class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)

        # Not enough flowers even if all of them bloom
        if m * k > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        def canMake(day):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                        if bouquets == m:
                            return True
                else:
                    # Adjacency is broken
                    flowers = 0

            return False

        while left < right:
            mid = (left + right) // 2

            if canMake(mid):
                right = mid
            else:
                left = mid + 1

        return left