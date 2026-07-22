class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0

        # Customers already satisfied
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        # Extra customers that can be satisfied in the first window
        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        # Slide the window
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                extra += customers[i]

            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra