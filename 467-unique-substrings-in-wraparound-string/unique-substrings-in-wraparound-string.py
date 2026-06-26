class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        longest = [0] * 26
        length = 0

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                length += 1
            else:
                length = 1

            index = ord(s[i]) - ord('a')
            longest[index] = max(longest[index], length)

        return sum(longest)