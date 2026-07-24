class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0] * 1001

        for passengers, start, end in trips:
            road[start] += passengers
            road[end] -= passengers

        current = 0

        for change in road:
            current += change
            if current > capacity:
                return False

        return True