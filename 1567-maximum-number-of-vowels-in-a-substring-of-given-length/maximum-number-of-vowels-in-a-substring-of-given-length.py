class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        answer = count

        # Move the window through the string
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            answer = max(answer, count)

        return answer