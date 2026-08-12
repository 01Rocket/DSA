class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        chars = list(palindrome)
        n = len(chars)

        # A single character cannot be made non-palindromic
        if n == 1:
            return ""

        # Change the first non-'a' character in the first half
        for i in range(n // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return ''.join(chars)

        # If all characters in the first half are 'a',
        # change the last character to 'b'
        chars[-1] = 'b'
        return ''.join(chars)