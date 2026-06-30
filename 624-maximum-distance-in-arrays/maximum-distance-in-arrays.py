class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]

        answer = 0

        # Compare every other array
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            # Find the maximum distance
            answer = max(answer, abs(current_max - min_value))
            answer = max(answer, abs(max_value - current_min))

            # Update overall minimum and maximum
            min_value = min(min_value, current_min)
            max_value = max(max_value, current_max)

        return answer