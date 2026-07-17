class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [float("inf")] * 26

        for word in words:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                common[i] = min(common[i], count[i])

        result = []

        for i in range(26):
            while common[i] > 0:
                result.append(chr(i + ord('a')))
                common[i] -= 1

        return result