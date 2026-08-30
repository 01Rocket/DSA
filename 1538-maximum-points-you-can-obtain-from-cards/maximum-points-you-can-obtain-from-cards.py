class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        # Total points of all cards
        total = sum(cardPoints)

        # We need to leave n-k cards in the middle
        window_size = n - k

        # Find the minimum sum of n-k consecutive cards
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum

        for i in range(window_size, n):
            window_sum += cardPoints[i]
            window_sum -= cardPoints[i - window_size]

            min_window = min(min_window, window_sum)

        # Maximum score = total - minimum middle part
        return total - min_window