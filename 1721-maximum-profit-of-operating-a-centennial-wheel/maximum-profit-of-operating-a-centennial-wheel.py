class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        profit = 0
        max_profit = 0
        rotations = 0
        answer = -1

        i = 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
                i += 1

            boarded = min(waiting, 4)
            waiting -= boarded

            rotations += 1
            profit += boarded * boardingCost - runningCost

            if profit > max_profit:
                max_profit = profit
                answer = rotations

        return answer