class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # The order of L and R should remain the same
        if start.replace("X", "") != result.replace("X", ""):
            return False

        i = 0
        j = 0
        n = len(start)

        while i < n and j < n:
            # Skip X characters
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1

            if i == n or j == n:
                break

            # L can only move left
            if start[i] == "L" and i < j:
                return False

            # R can only move right
            if start[i] == "R" and i > j:
                return False

            i += 1
            j += 1

        return True