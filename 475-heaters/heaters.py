class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0

        for house in houses:
            index = bisect_left(heaters, house)

            left = float('inf')
            right = float('inf')

            if index > 0:
                left = house - heaters[index - 1]

            if index < len(heaters):
                right = heaters[index] - house

            radius = max(radius, min(left, right))

        return radius