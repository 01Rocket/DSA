class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # Function to count palindromes from the center
        def expand(left, right):
            nonlocal count

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        # Check every possible center
        for i in range(len(s)):
            expand(i, i)       # Odd-length palindromes
            expand(i, i + 1)   # Even-length palindromes

        return count