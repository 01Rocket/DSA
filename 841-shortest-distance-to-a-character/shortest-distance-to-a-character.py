class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [float('inf')] * n

        # Check distance from the left side
        distance = float('inf')
        for i in range(n):
            if s[i] == c:
                distance = 0
            else:
                distance += 1

            answer[i] = distance

        # Check distance from the right side
        distance = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                distance = 0
            else:
                distance += 1

            answer[i] = min(answer[i], distance)

        return answer