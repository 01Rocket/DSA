class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        lastPerson = -1
        maxDistance = 0

        for i in range(n):
            if seats[i] == 1:
                if lastPerson == -1:
                    # Empty seats before the first person
                    maxDistance = i
                else:
                    # Empty seats between two people
                    maxDistance = max(maxDistance, (i - lastPerson) // 2)

                lastPerson = i

        # Empty seats after the last person
        maxDistance = max(maxDistance, n - 1 - lastPerson)

        return maxDistance