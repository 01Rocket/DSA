class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        result = list(s)
        totalShift = 0

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            totalShift = (totalShift + shifts[i]) % 26

            # Shift the current character
            newChar = (ord(result[i]) - ord('a') + totalShift) % 26
            result[i] = chr(newChar + ord('a'))

        return "".join(result)